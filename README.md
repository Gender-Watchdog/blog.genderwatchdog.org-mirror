# Gender Watchdog Blog - Jekyll Mirror

**Primary Site:** [blog.genderwatchdog.org](https://blog.genderwatchdog.org)

This repository contains the Jekyll source for the Gender Watchdog Blog, documenting institutional capture in Korea through the Dongguk University case: academic fraud, racialized sexual violence, institutional betrayal, and press gagging via weaponized defamation law that criminalizes truthful testimony.

## 🌐 Multi-Language Support

The blog is available in six languages:
- 🇺🇸 [English](https://blog.genderwatchdog.org/en/) (89 posts)
- 🇰🇷 [한국어](https://blog.genderwatchdog.org/ko/) (27 posts)
- 🇯🇵 [日本語](https://blog.genderwatchdog.org/ja/) (29 posts)
- 🇨🇳 [简体中文](https://blog.genderwatchdog.org/zh-cn/) (25 posts)
- 🇭🇰 [繁體中文](https://blog.genderwatchdog.org/zh-tw/) (27 posts)
- 🌏 [Other Languages](https://blog.genderwatchdog.org/other/) (8 posts: French, Indonesian, Russian, Vietnamese, Kazakh, Mongolian, Thai, Uzbek)

**Total:** 205 blog posts + 7 utility pages

## 📖 About This Project

This site serves as a censorship-resistant mirror of our investigative documentation, which experienced a major traffic spike (most likely AI scrape bots) 48 hours before APEC Economic Leaders' Week (Oct.27 to Nov.1, 2025) in Gyeongju, South Korea 2025. We migrated to GitHub Pages to ensure:

- **Transparency**: Any takedown requires public legal process
- **Resilience**: Multiple mirrors prevent quiet censorship
- **Accountability**: GitHub's scale makes suppression politically expensive
- **Documentation**: The migration itself proves censorship attempts

## 🛠️ Technical Stack

- **Generator**: Jekyll 4.4.1
- **Hosting**: GitHub Pages
- **Domain**: blog.genderwatchdog.org (via Namecheap)
- **Analytics**: Fathom Analytics (privacy-focused, GDPR compliant)
- **License**: Dual License (Apache 2.0 / CC BY-NC-ND 4.0) - see below

## ⚖️ Legal & Licensing

### Truthful Posture (Not an NGO)
This project is an **independent, volunteer-run initiative** and pre-incorporation social enterprise.
*   **We are NOT a registered non-profit organization or NGO.**
*   **We DO NOT solicit tax-exempt donations.**
*   **We operate independently of our supporters.** Organizations like EROC express solidarity but provide no funding, oversight, or editorial direction.

### Dual-License Strategy
To protect our investigative integrity while keeping our tools open:
*   **Code (Scripts, CSS, Templates):** [Apache 2.0](LICENSE) - Free to use and audit.
*   **Content (Reports, Data, Images):** [CC BY-NC-ND 4.0](LICENSE-CONTENT) - Attribution required, Non-Commercial use only, **No Derivatives** allowed (you cannot alter our reports to change the findings).

## 📂 Repository Structure

```
.
├── _config.yml              # Jekyll configuration
├── _layouts/                # Page templates
│   ├── default.html         # Base layout with SEO & footer
│   ├── home.html            # Homepage layout
│   └── post.html            # Individual post layout
├── _posts/                  # Blog posts (205 files)
│   └── YYYY-MM-DD-slug.md   # Format: date-slug.md
├── assets/
│   └── css/style.css        # Styling with CJK font support
├── en/                      # Language archive pages
├── ko/
├── ja/
├── zh-cn/
├── zh-tw/
├── other/
├── index.md                 # Homepage (timeline)
├── about.md                 # Utility pages
├── contact.md
├── disclaimer.md
├── youtube.md
├── twitter.md
├── where-to-read.md
├── qr-code.md
├── CNAME                    # Custom domain config
├── Gemfile                  # Ruby dependencies
└── convert_csv_to_posts.py  # CSV to Jekyll converter
```

## 🚀 Local Development

### Prerequisites

- Ruby 3.0+
- Bundler
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/Gender-Watchdog/blog.genderwatchdog.org-mirror.git
cd blog.genderwatchdog.org-mirror

# Install dependencies
bundle install --path vendor/bundle

# Serve locally
bundle exec jekyll serve --host 0.0.0.0 --port 4000

# Visit: http://localhost:4000
```

### Adding New Posts

**Method 1: Manual Creation**

Create a new file in `_posts/` with the format: `YYYY-MM-DD-slug.md`

```yaml
---
layout: post
title: "Your Post Title"
slug: "your-post-slug"
date: 2025-10-25T12:00:00+00:00
lang: en  # or ko, ja, zh-cn, zh-tw, other
meta_description: "Optional description"
---

Your content here in Markdown...
```

**Method 2: CSV Conversion (Bulk)**

If you have a Bear Blog CSV export:

```bash
# Place CSV at: secret-files/from-bearblog/10252025-post_export.csv
python3 convert_csv_to_posts.py

# This generates all posts with:
# - Automatic language detection
# - Proper frontmatter
# - Sanitized filenames
```

### Language Detection

The converter automatically detects language from:
- Slug suffixes: `-ja`, `-ko`, `-zh-cn`, `-zh-tw`
- Title Unicode ranges (Hangul, Hiragana/Katakana, CJK)
- Specific language prefixes (INVESTIGASI, РАЗОБЛАЧЕНИЕ, etc.)
- Defaults to English

## 📦 Deployment

The site auto-deploys via GitHub Actions on every push to `master`:

1. **Push changes:**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin master
   ```

2. **GitHub Pages builds automatically** (1-2 minutes)

3. **Site updates** within 5-10 minutes at blog.genderwatchdog.org

### Custom Domain Setup

See [`secret-files/deploy-to-ghpages.md`](secret-files/deploy-to-ghpages.md) for detailed instructions.

## 🔒 Security & Privacy

- **HTTPS**: Enforced via GitHub Pages (Let's Encrypt)
- **Analytics**: Privacy-focused Fathom (no cookies, no personal data)
- **No tracking**: No Google Analytics, Facebook Pixel, or similar
- **GDPR compliant**: Respects international data protection

## 🌟 Features

### SEO Optimization
- Multi-language meta tags (ko, ja, zh-CN, zh-TW)
- Structured data (JSON-LD)
- Open Graph tags
- Twitter Card metadata
- Canonical URLs
- Sitemap generation

### Accessibility
- Semantic HTML
- Proper heading hierarchy
- Alt text for images
- Responsive design
- CJK font optimization

### Multi-language Support
- Separate archive pages per language
- Language-specific permalinks (/:lang/:slug/)
- hreflang tags for SEO
- Unicode-aware search

## 📚 Related Projects

- **Timeline Website**: [genderwatchdog.org](https://genderwatchdog.org)
- **Evidence Repository**: [github.com/Gender-Watchdog/genderwatchdog_metookorea2025](https://github.com/Gender-Watchdog/genderwatchdog_metookorea2025)
- **Bear Blog Mirror**: [genderwatchdog.bearblog.dev](https://genderwatchdog.bearblog.dev)

## 🤝 Support & Coalition

We are honored to receive support from:
- [End Rape On Campus (EROC)](https://twitter.com/EndRapeOnCampus)

## 📞 Contact

- **Email**: genderwatchdog@proton.me
- **Twitter**: [@Gender_Watchdog](https://twitter.com/Gender_Watchdog)
- **Mastodon**: [@genderwatchdog@mastodon.social](https://mastodon.social/@genderwatchdog)
- **YouTube**: [Gender Watchdog Channel](https://www.youtube.com/@GenderWatchdog)

## ⚖️ License

**Content License**: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- ✅ Share and adapt with attribution
- ✅ Non-commercial use
- ✅ Share-alike required
- ❌ Commercial use prohibited

**Code License**: MIT (Jekyll configuration and scripts)

## 🛡️ Why This Repository Matters

This repository documents systematic institutional failures and serves as evidence of censorship attempts. The migration to GitHub Pages ensures:

1. **Public record**: All takedown attempts become public via GitHub transparency reports
2. **Tech community oversight**: Censorship attempts trigger immediate scrutiny
3. **Geopolitical leverage**: Targeting Microsoft-owned infrastructure has consequences
4. **Streisand effect**: Suppression attempts amplify the story

**The repository itself is part of the evidence.**

## 📊 Statistics

- **Total Posts**: 205
- **Languages**: 6
- **Contributors**: Gender Watchdog Research Collective
- **First Publish**: April 2025
- **Migration to GitHub**: October 2025 (after censorship attempt)
- **Uptime**: 99.9%+ (GitHub Pages SLA)

## 🔗 Quick Links

- [English Posts](https://blog.genderwatchdog.org/en/)
- [About Gender Watchdog](https://blog.genderwatchdog.org/about/)
- [Contact Us](https://blog.genderwatchdog.org/contact/)
- [Deployment Guide](secret-files/deploy-to-ghpages.md)
- [Censorship Documentation](secret-files/censorship-docs/)

---

**Built with Jekyll • Hosted on GitHub Pages • Powered by Truth**

*"Transparency protects survivors. Censorship protects perpetrators."*

© 2025 Gender Watchdog Research Collective. All rights reserved.

