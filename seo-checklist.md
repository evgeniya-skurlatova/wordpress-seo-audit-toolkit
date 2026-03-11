# ✅ WordPress Technical SEO Checklist

A structured checklist for auditing WordPress sites. Work through each section top to bottom.

**Legend:** 🔴 Critical · 🟠 Important · 🟡 Medium · 🟢 Good to have

---

## 1. robots.txt

- [ ] 🔴 File is accessible at `/robots.txt`
- [ ] 🔴 Contains `Sitemap:` directive pointing to sitemap index
- [ ] 🔴 `/wp-admin/` is blocked for all bots
- [ ] 🟠 `/wp-login.php` is blocked
- [ ] 🟠 No critical sections accidentally blocked (uploads, blog, key pages)
- [ ] 🟡 Separate rules for Googlebot vs other crawlers if needed

**Quick check:**
```
https://yoursite.com/robots.txt
```

---

## 2. Sitemap.xml

- [ ] 🔴 Sitemap index accessible at `/sitemap_index.xml`
- [ ] 🔴 All sub-sitemaps return 200 status
- [ ] 🟠 `lastmod` dates are up to date (no sub-sitemap older than 6 months without review)
- [ ] 🟠 No URLs returning 404 inside sitemaps
- [ ] 🟠 Image sitemaps present if site is image-heavy
- [ ] 🟡 Sitemap submitted to Google Search Console
- [ ] 🟡 Sitemap submitted to Yandex Webmaster (for .ru domains)

**Sub-sitemaps to verify for Yoast SEO:**
```
/post-sitemap.xml
/page-sitemap.xml
/category-sitemap.xml
```

---

## 3. hreflang & Multilingual

- [ ] 🔴 hreflang tags present on all language versions
- [ ] 🔴 Each language page references all other language versions (reciprocal)
- [ ] 🔴 `x-default` hreflang set for the fallback version
- [ ] 🟠 Language versions on different domains use cross-domain hreflang
- [ ] 🟠 No language version returns 404 that is referenced in hreflang
- [ ] 🟡 hreflang consistent in sitemap AND in `<head>`

**Example of correct hreflang setup:**
```html
<link rel="alternate" hreflang="ru" href="https://site.ru/" />
<link rel="alternate" hreflang="en" href="https://site.com/" />
<link rel="alternate" hreflang="x-default" href="https://site.com/" />
```

---

## 4. Meta Tags

- [ ] 🔴 Every page has a unique `<title>`
- [ ] 🔴 Title length: 50–65 characters
- [ ] 🔴 Every page has a unique meta description
- [ ] 🔴 Meta description length: 120–160 characters
- [ ] 🟠 No duplicate titles across pages
- [ ] 🟠 Canonical tag present and pointing to correct URL
- [ ] 🟠 OG tags (og:title, og:description, og:image) for social sharing
- [ ] 🟡 Twitter Card meta tags

**Check title length quickly:**
```python
# See scripts/parse_meta.py
```

---

## 5. URL Structure

- [ ] 🔴 No URLs with technical artifacts in slugs (random IDs, hashes)
- [ ] 🔴 301 redirects in place for any changed URLs
- [ ] 🟠 Consistent transliteration standard for non-Latin URLs
- [ ] 🟠 No URLs with uppercase letters
- [ ] 🟠 No trailing slashes inconsistency (pick one and stick to it)
- [ ] 🟡 URL depth: key pages no deeper than 3 clicks from homepage
- [ ] 🟡 No underscores in URLs (use hyphens)

---

## 6. Page Speed & Core Web Vitals

- [ ] 🔴 LCP (Largest Contentful Paint) < 2.5s
- [ ] 🔴 CLS (Cumulative Layout Shift) < 0.1
- [ ] 🔴 INP (Interaction to Next Paint) < 200ms
- [ ] 🟠 No GIF files used for animation (convert to WebM/WebP)
- [ ] 🟠 All images have explicit `width` and `height` attributes
- [ ] 🟠 Background video uses `preload="none"`
- [ ] 🟠 Images in modern formats (WebP or AVIF)
- [ ] 🟡 Caching plugin configured (WP Rocket, LiteSpeed Cache, W3 Total Cache)
- [ ] 🟡 CDN in use for static assets

**Test here:**
```
https://pagespeed.web.dev/
```

---

## 7. Indexability

- [ ] 🔴 Homepage is indexable (no noindex tag)
- [ ] 🔴 Key landing pages are indexable
- [ ] 🟠 Thin content pages (< 300 words, no unique value) have noindex or are enriched
- [ ] 🟠 /video sub-pages without text content are reviewed
- [ ] 🟠 Tag and author archive pages reviewed for duplicate content
- [ ] 🟡 Pagination handled correctly (rel="next/prev" or canonical)
- [ ] 🟡 Search results pages blocked from indexing

---

## 8. Structured Data (Schema.org)

- [ ] 🟠 `Organization` or `LocalBusiness` on homepage
- [ ] 🟠 `SoftwareApplication` for SaaS/app sites
- [ ] 🟠 `Article` or `BlogPosting` on blog posts
- [ ] 🟠 `FAQPage` if FAQ section exists
- [ ] 🟡 `BreadcrumbList` on inner pages
- [ ] 🟡 `Product` on product/pricing pages

**Validate here:**
```
https://search.google.com/test/rich-results
```

---

## 9. WordPress-specific

- [ ] 🔴 WordPress version is up to date
- [ ] 🔴 All plugins up to date
- [ ] 🟠 Yoast SEO (or equivalent) properly configured
- [ ] 🟠 XML sitemap generation enabled in SEO plugin
- [ ] 🟠 No sensitive files exposed (`wp-config.php`, `.env`)
- [ ] 🟡 REST API restricted if not in use
- [ ] 🟡 `readme.html` and `license.txt` removed or blocked

---

## 📊 Audit Summary Template

| Area | Status | Priority | Notes |
|---|---|---|---|
| robots.txt | ⬜ | 🔴 | |
| Sitemap | ⬜ | 🔴 | |
| hreflang | ⬜ | 🔴 | |
| Meta tags | ⬜ | 🟠 | |
| URL structure | ⬜ | 🟠 | |
| Page speed | ⬜ | 🟠 | |
| Indexability | ⬜ | 🟡 | |
| Structured data | ⬜ | 🟡 | |
| WP-specific | ⬜ | 🟡 | |
