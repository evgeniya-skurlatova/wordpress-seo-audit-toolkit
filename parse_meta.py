#!/usr/bin/env python3
"""
parse_meta.py
Fetches a page and reports on key SEO meta tags:
title, description, canonical, robots, og tags, hreflang.

Usage:
    python parse_meta.py https://yoursite.com/
"""

import sys
import requests
from html.parser import HTMLParser

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self._in_title = False
        self.description = ''
        self.canonical = ''
        self.robots = ''
        self.og = {}
        self.hreflang = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self._in_title = True
        elif tag == 'meta':
            name = attrs.get('name', '').lower()
            prop = attrs.get('property', '').lower()
            content = attrs.get('content', '')
            if name == 'description':
                self.description = content
            elif name == 'robots':
                self.robots = content
            elif prop.startswith('og:'):
                self.og[prop] = content
        elif tag == 'link':
            rel = attrs.get('rel', '').lower()
            if rel == 'canonical':
                self.canonical = attrs.get('href', '')
            elif rel == 'alternate' and attrs.get('hreflang'):
                self.hreflang.append({
                    'hreflang': attrs.get('hreflang'),
                    'href': attrs.get('href', '')
                })

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

def check(label, value, ok_range=None, warn_empty=True):
    if not value:
        if warn_empty:
            print(f"  ❌ {label}: MISSING")
        return
    length = len(value)
    if ok_range:
        lo, hi = ok_range
        icon = '✅' if lo <= length <= hi else '⚠️ '
        print(f"  {icon} {label} ({length} chars): {value[:80]}{'...' if len(value)>80 else ''}")
    else:
        print(f"  ✅ {label}: {value[:100]}{'...' if len(value)>100 else ''}")

def parse_meta(url):
    print(f"\n🔍 Parsing meta tags: {url}\n")
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'SEO-Audit-Bot/1.0'})
    except Exception as e:
        print(f"  ❌ Could not fetch page: {e}")
        return

    if r.status_code != 200:
        print(f"  ❌ HTTP {r.status_code}")
        return

    parser = MetaParser()
    parser.feed(r.text)

    print("── Basic SEO ─────────────────────────────")
    check('Title', parser.title.strip(), ok_range=(50, 65))
    check('Meta description', parser.description, ok_range=(120, 160))
    check('Canonical', parser.canonical)
    check('Robots', parser.robots, warn_empty=False) or print("  ✅ Robots: (not set — indexable by default)")

    print("\n── Open Graph ────────────────────────────")
    for key in ['og:title', 'og:description', 'og:image', 'og:type']:
        check(key, parser.og.get(key, ''))

    print("\n── hreflang ──────────────────────────────")
    if parser.hreflang:
        for h in parser.hreflang:
            print(f"  ✅ [{h['hreflang']}] {h['href']}")
        has_default = any(h['hreflang'] == 'x-default' for h in parser.hreflang)
        if not has_default:
            print("  ⚠️  x-default hreflang is MISSING")
    else:
        print("  ⚠️  No hreflang tags found")

    print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python parse_meta.py <url>")
        sys.exit(1)
    parse_meta(sys.argv[1])
