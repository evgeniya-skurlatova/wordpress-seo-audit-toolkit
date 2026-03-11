# hreflang Templates for Multilingual WordPress Sites

## Single domain, multiple languages (subdirectory)
```html
<link rel="alternate" hreflang="en" href="https://site.com/en/" />
<link rel="alternate" hreflang="ru" href="https://site.com/ru/" />
<link rel="alternate" hreflang="de" href="https://site.com/de/" />
<link rel="alternate" hreflang="x-default" href="https://site.com/" />
```

## Multiple domains (one language per domain)
```html
<link rel="alternate" hreflang="ru" href="https://site.ru/" />
<link rel="alternate" hreflang="en" href="https://site.com/" />
<link rel="alternate" hreflang="pl" href="https://site.com/pol/" />
<link rel="alternate" hreflang="uk" href="https://site.com/ukr/" />
<link rel="alternate" hreflang="fr" href="https://site.com/fra/" />
<link rel="alternate" hreflang="es" href="https://site.com/spa/" />
<link rel="alternate" hreflang="de" href="https://site.com/deu/" />
<link rel="alternate" hreflang="tr" href="https://site.com/tur/" />
<link rel="alternate" hreflang="zh-Hans" href="https://site.com/chn/" />
<link rel="alternate" hreflang="x-default" href="https://site.com/" />
```

## Rules
# 1. Every page must reference ALL language versions — including itself
# 2. x-default must always be included
# 3. hreflang links must be reciprocal (A links to B, B links back to A)
# 4. Use BCP 47 language codes: en, ru, de, zh-Hans, pt-BR etc.
# 5. Place in <head> on every page, OR include in sitemap
