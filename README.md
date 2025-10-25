# Gender Watchdog Blog - GitHub Pages Mirror

This is a Jekyll-based mirror of the Gender Watchdog blog, originally hosted on Bear Blog. The site is deployed to GitHub Pages and accessible at **blog.genderwatchdog.org**.

## Structure

```
├── _config.yml           # Jekyll configuration
├── _layouts/             # Page templates
│   ├── default.html      # Base layout with header/footer
│   ├── post.html         # Individual post layout
│   └── home.html         # Homepage layout
├── _posts/               # Blog posts (222 posts)
├── assets/css/           # Stylesheets
│   └── style.css         # Main stylesheet with multi-language support
├── en/                   # English posts archive
├── zh-cn/                # Simplified Chinese posts archive
├── zh-tw/                # Traditional Chinese posts archive
├── ja/                   # Japanese posts archive
├── ko/                   # Korean posts archive
├── other/                # Other languages (French, Indonesian, Russian, etc.)
├── index.md              # Homepage with timeline
├── CNAME                 # Custom domain configuration
├── Gemfile               # Ruby dependencies
└── convert_csv_to_posts.py  # Conversion script

```

## Post Statistics

- **Total posts created**: 222
- **English (en)**: 70 posts
- **Simplified Chinese (zh-cn)**: 23 posts
- **Traditional Chinese (zh-tw)**: 26 posts
- **Japanese (ja)**: 28 posts
- **Korean (ko)**: 26 posts
- **Other languages**: 49 posts (French, Indonesian, Russian, Vietnamese, Kazakh, Mongolian, Thai, Uzbek)

## Language Detection

Posts are categorized by language based on slug suffixes:
- English: no suffix (default)
- Japanese: `-ja`
- Korean: `-ko`
- Simplified Chinese: `-zh-cn`, `-zh-ch`, or `hans`
- Traditional Chinese: `-zh-tw` or `hant`
- Other languages: detected by specific patterns

## Local Development

### Prerequisites
- Ruby 2.7+
- Bundler

### Setup
```bash
bundle install
```

### Build and Serve
```bash
bundle exec jekyll serve
```

Visit http://localhost:4000 to view the site locally.

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

### Custom Domain Setup
1. GitHub repository settings:
   - Repository: blog.genderwatchdog.org-mirror
   - Settings → Pages → Custom domain: blog.genderwatchdog.org
   
2. DNS configuration at Namecheap:
   ```
   Type: CNAME
   Host: blog
   Value: gender-watchdog.github.io
   TTL: Automatic
   ```

## Conversion Script

To re-run the CSV to Jekyll conversion:

```bash
python3 convert_csv_to_posts.py
```

The script reads from `secret-files/from-bearblog/10252025-post_export.csv` and outputs to `_posts/`.

## Features

- **Multi-language support**: Proper font rendering for CJK languages
- **Mobile responsive**: Optimized for all screen sizes
- **SEO optimized**: Meta tags, sitemap, and RSS feed
- **Censorship resistant**: Multiple mirrors maintained
- **Archive notices**: Links to GitHub evidence repository

## Mirror Sites

- Primary: https://blog.genderwatchdog.org (GitHub Pages)
- Mirror: https://genderwatchdog.bearblog.dev (Bear Blog)
- Substack: https://genderwatchdog.substack.com

## License

Content: CC BY-NC-SA 4.0  
Code: MIT License

## Contact

Email: genderwatchdog@proton.me  
Twitter: @Gender_Watchdog  
GitHub: https://github.com/Gender-Watchdog

