#!/usr/bin/env python3
"""
check_sitemap.py
Checks a WordPress sitemap index: fetches all sub-sitemaps,
validates HTTP status and lastmod freshness.

Usage:
    python check_sitemap.py https://yoursite.com/sitemap_index.xml
"""

import sys
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

NS = {
    'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'
}

def fetch(url):
    try:
        r = requests.get(url, timeout=10, headers={'User-Agent': 'SEO-Audit-Bot/1.0'})
        return r
    except Exception as e:
        return None

def parse_date(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except:
        return None

def check_sitemap_index(index_url):
    print(f"\n🔍 Checking sitemap index: {index_url}\n")
    r = fetch(index_url)
    if not r:
        print(f"  ❌ Could not reach {index_url}")
        return

    if r.status_code != 200:
        print(f"  ❌ HTTP {r.status_code} — sitemap index not accessible")
        return

    print(f"  ✅ Index accessible (HTTP 200)\n")

    try:
        root = ET.fromstring(r.text)
    except ET.ParseError as e:
        print(f"  ❌ XML parse error: {e}")
        return

    sitemaps = root.findall('sm:sitemap', NS)
    print(f"  Found {len(sitemaps)} sub-sitemap(s):\n")

    now = datetime.now(timezone.utc)
    issues = []

    for sm in sitemaps:
        loc = sm.findtext('sm:loc', namespaces=NS)
        lastmod_str = sm.findtext('sm:lastmod', namespaces=NS)
        lastmod = parse_date(lastmod_str)

        sub_r = fetch(loc)
        status = sub_r.status_code if sub_r else 'ERROR'
        status_icon = '✅' if status == 200 else '❌'

        age_str = ''
        age_icon = ''
        if lastmod:
            days_old = (now - lastmod).days
            age_str = f"  lastmod: {lastmod_str[:10]} ({days_old}d ago)"
            if days_old > 180:
                age_icon = ' ⚠️  STALE'
                issues.append(f"  ⚠️  {loc} — not updated in {days_old} days")

        print(f"  {status_icon} [{status}] {loc}")
        if age_str:
            print(f"         {age_str}{age_icon}")

    if issues:
        print(f"\n⚠️  Issues found:")
        for i in issues:
            print(i)
    else:
        print(f"\n✅ All sub-sitemaps look healthy!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python check_sitemap.py <sitemap_index_url>")
        sys.exit(1)
    check_sitemap_index(sys.argv[1])
