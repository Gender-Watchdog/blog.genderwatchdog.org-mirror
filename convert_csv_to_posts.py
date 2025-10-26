#!/usr/bin/env python3
"""
Convert Bear Blog CSV export to Jekyll posts with multi-language support
"""

import csv
import os
import re
import sys
from datetime import datetime

# Increase CSV field size limit to handle large posts
csv.field_size_limit(sys.maxsize)


def detect_language(slug, title):
    """Detect language from slug suffix patterns and title content"""
    slug_lower = slug.lower()
    
    # Check slug suffix first
    # Japanese
    if slug_lower.endswith('-ja'):
        return 'ja'
    
    # Korean (including -ko-new variant)
    if slug_lower.endswith('-ko') or slug_lower.endswith('-ko-new'):
        return 'ko'
    
    # Simplified Chinese
    if slug_lower.endswith('-zh-cn') or slug_lower.endswith('-zh-ch') or slug_lower.endswith('-hans'):
        return 'zh-cn'
    
    # Traditional Chinese  
    if slug_lower.endswith('-zh-tw') or slug_lower.endswith('-hant'):
        return 'zh-tw'
    
    # Check for other language patterns - ONLY as suffixes at the end
    other_lang_suffixes = ['-id', '-ru', '-vi', '-kk', '-mn', '-th', '-uz', '-fr']
    for suffix in other_lang_suffixes:
        if slug_lower.endswith(suffix):
            return 'other'
    
    # Check for French-specific patterns in slug
    if 'objet-preoccupations' in slug_lower or 'luniversite' in slug_lower:
        return 'other'
    
    # Check title for non-English scripts
    if not title:
        return 'en'
    
    # Japanese (Hiragana, Katakana, some Kanji ranges)
    if re.search(r'[\u3040-\u309F\u30A0-\u30FF]', title):
        return 'ja'
    
    # Korean (Hangul)
    if re.search(r'[\uAC00-\uD7AF\u1100-\u11FF\u3130-\u318F]', title):
        return 'ko'
    
    # Check for specific language prefixes in title (for "other" languages)
    # Note: "EXPOSÉ" is commonly used in English, so not included here
    if title.startswith(('INVESTIGASI:', 'ĐIỀU TRA:', 'ЗЕРТТЕУ:', 'ИЛРҮҮЛЭЛТ:', 
                         'РАЗОБЛАЧЕНИЕ:', 'การเปิดโปง:', 'TADQIQOT:')):
        return 'other'
    
    # Chinese detection (more complex due to overlapping ranges)
    # Check if title has CJK Unified Ideographs
    cjk_match = re.search(r'[\u4E00-\u9FFF]', title)
    if cjk_match:
        # Try to distinguish between Simplified and Traditional
        # Check for Traditional-specific characters or simplified indicators
        if '新聞稿' in title or '資訊' in title or '國際' in title:
            return 'zh-tw'
        # Default CJK to Simplified Chinese if can't determine
        return 'zh-cn'
    
    # Default to English
    return 'en'


def is_delimiter_post(title, content):
    """Check if this is a delimiter post that should be filtered out"""
    # KEEP these delimiter posts (they are category markers we want)
    if 'Researched by AI' in title or 'Researched by Human Researchers' in title:
        return False
    
    # Delimiter posts to REMOVE
    delimiter_patterns = [
        r'^-+\s*BREAKING NEWS\s*-+$',
        r'^-+\s*Title IX\s*-+$',
        r'^-+\s*Press Releases\s*-+$',
        r'^-+\s*简体中文\s*-+$',
        r'^-+\s*繁體中文\s*-+$',
        r'^-+\s*日本語\s*-+$',
        r'^-+\s*한국어\s*-+$',
        r'^-+\s*English \+ Fr\s*-+$',
        r'^-+\s*Articles\s*-+$',
        r'^-+\s*Other\s*-+$',
    ]
    
    for pattern in delimiter_patterns:
        if re.match(pattern, title.strip()):
            return True
    
    # Also check if content is empty (another sign of delimiter)
    if not content or not content.strip():
        if any(kw in title for kw in ['---', 'BREAKING', 'Title IX', 'Press Release', 
                                        '简体中文', '繁體中文', '日本語', '한국어', 
                                        'English + Fr', 'Articles', 'Other']):
            return True
    
    return False


def is_utility_page(title, slug):
    """Check if this should be a standalone page instead of a post"""
    utility_slugs = [
        'qr-code-qr',
        'about-gender-watchdog',
        'disclaimer-for-source-links',
        'disclaimer',
        'contact',
        'youtube-channel',
        'where-else-to-read-gender-watchdog',
        'gender-watchdogs-official-x-account',
        'web-archive-access',
    ]
    
    return slug.lower() in utility_slugs


def create_utility_page(title, slug, content, published_date):
    """Create a standalone Jekyll page"""
    # Map slugs to cleaner permalinks
    permalink_map = {
        'qr-code-qr': 'qr-code',
        'about-gender-watchdog': 'about',
        'disclaimer-for-source-links': 'disclaimer',
        'youtube-channel': 'youtube',
        'where-else-to-read-gender-watchdog': 'where-to-read',
        'gender-watchdogs-official-x-account': 'twitter',
        'web-archive-access': 'web-archive',
    }
    
    permalink = permalink_map.get(slug, slug)
    filename = f"{permalink}.md"
    
    frontmatter = f"""---
layout: default
title: {escape_yaml_string(title)}
permalink: /{permalink}/
---

"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write(content)
    
    return filename


def sanitize_filename(slug, date_str):
    """Create Jekyll-friendly filename: YYYY-MM-DD-slug.md"""
    # Extract YYYY-MM-DD from ISO format date
    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    date_prefix = date_obj.strftime('%Y-%m-%d')
    
    # Clean slug: remove special characters, keep hyphens
    clean_slug = re.sub(r'[^\w\s-]', '', slug)
    clean_slug = re.sub(r'[-\s]+', '-', clean_slug)
    clean_slug = clean_slug.strip('-')
    
    return f"{date_prefix}-{clean_slug}.md"


def escape_yaml_string(s):
    """Escape strings for YAML frontmatter"""
    if not s:
        return '""'
    
    # If string contains special YAML characters, wrap in quotes
    # Added * to prevent YAML alias parsing errors
    if any(c in s for c in [':', '#', '"', "'", '\n', '@', '`', '*']):
        # Escape double quotes
        s = s.replace('"', '\\"')
        return f'"{s}"'
    
    return s


def convert_csv_to_jekyll(csv_file, output_dir='_posts'):
    """Convert Bear Blog CSV to Jekyll posts"""
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    stats = {
        'total': 0,
        'published': 0,
        'pages_skipped': 0,
        'delimiters_skipped': 0,
        'utility_pages_created': 0,
        'en': 0,
        'zh-cn': 0,
        'zh-tw': 0,
        'ja': 0,
        'ko': 0,
        'other': 0,
        'errors': []
    }
    
    print(f"Reading CSV from: {csv_file}")
    print(f"Output directory: {output_dir}")
    print("-" * 60)
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
            stats['total'] += 1
            
            # Skip if not published
            if row.get('publish', '').strip() != 'True':
                continue
            
            # Skip if it's a page
            if row.get('is page', '').strip() == 'True':
                stats['pages_skipped'] += 1
                continue
            
            try:
                # Extract metadata
                title = row.get('title', '').strip()
                slug = row.get('slug', '').strip()
                
                # Use alias as fallback slug
                if not slug:
                    slug = row.get('alias', '').strip()
                
                if not slug or not title:
                    print(f"Warning: Row {row_num} missing title or slug, skipping")
                    continue
                
                published_date = row.get('published date', '').strip()
                if not published_date:
                    print(f"Warning: Row {row_num} missing published date, skipping")
                    continue
                
                content = row.get('content', '')
                canonical_url = row.get('canonical url', '').strip()
                meta_description = row.get('meta description', '').strip()
                
                # Skip delimiter posts (except AI/Human Researchers which have content)
                if is_delimiter_post(title, content):
                    print(f"Skipping delimiter post: {title}")
                    stats['delimiters_skipped'] += 1
                    continue
                
                # Handle utility pages separately
                if is_utility_page(title, slug):
                    filename = create_utility_page(title, slug, content, published_date)
                    print(f"Created utility page: {filename}")
                    stats['utility_pages_created'] += 1
                    continue
                
                # Detect language from slug and title
                lang = detect_language(slug, title)
                stats[lang] += 1
                
                # Create filename
                filename = sanitize_filename(slug, published_date)
                filepath = os.path.join(output_dir, filename)
                
                # Create frontmatter
                frontmatter_lines = [
                    '---',
                    f'layout: post',
                    f'title: {escape_yaml_string(title)}',
                    f'slug: "{slug}"',  # Always quote slug to ensure it's treated as string
                    f'date: {published_date}',
                    f'lang: {lang}'
                ]
                
                if canonical_url:
                    frontmatter_lines.append(f'canonical_url: {canonical_url}')
                
                if meta_description:
                    frontmatter_lines.append(f'meta_description: {escape_yaml_string(meta_description)}')
                
                frontmatter_lines.append('---')
                
                # Write the post
                with open(filepath, 'w', encoding='utf-8') as post_file:
                    post_file.write('\n'.join(frontmatter_lines))
                    post_file.write('\n\n')
                    post_file.write(content)
                
                stats['published'] += 1
                
                # Print progress every 100 posts
                if stats['published'] % 100 == 0:
                    print(f"Processed {stats['published']} posts...")
                
            except Exception as e:
                error_msg = f"Error processing row {row_num}: {str(e)}"
                print(error_msg)
                stats['errors'].append(error_msg)
                continue
    
    # Print summary
    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE")
    print("=" * 60)
    print(f"Total rows in CSV: {stats['total']}")
    print(f"Published posts created: {stats['published']}")
    print(f"Utility pages created: {stats['utility_pages_created']}")
    print(f"Delimiter posts skipped: {stats['delimiters_skipped']}")
    print(f"Bear Blog pages skipped: {stats['pages_skipped']}")
    print(f"\nPosts by language:")
    print(f"  English (en):            {stats['en']}")
    print(f"  Simplified Chinese (zh-cn): {stats['zh-cn']}")
    print(f"  Traditional Chinese (zh-tw): {stats['zh-tw']}")
    print(f"  Japanese (ja):           {stats['ja']}")
    print(f"  Korean (ko):             {stats['ko']}")
    print(f"  Other languages:         {stats['other']}")
    
    if stats['errors']:
        print(f"\nErrors encountered: {len(stats['errors'])}")
        print("First 5 errors:")
        for error in stats['errors'][:5]:
            print(f"  - {error}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    csv_path = 'secret-files/from-bearblog/10252025-post_export.csv'
    output_path = '_posts'
    
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        print("Please make sure the Bear Blog export CSV is in the correct location.")
        exit(1)
    
    convert_csv_to_jekyll(csv_path, output_path)

