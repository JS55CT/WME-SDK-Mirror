"""
build-url-list.py
=================
Discovers all documentation page URLs from the Waze SDK TypeDoc SPA.

Problem: The site is a Single-Page App -- no static links in HTML.
Solution: TypeDoc stores its full sidebar navigation tree in assets/navigation.js
          as window.navigationData = "<base64+zlib JSON>".
          We decode that tree and walk every 'path' entry to get the complete URL list.

Output:
  - url-list.txt       -- one URL per line, ready for wget / requests
  - url-list-paths.txt -- relative paths only (e.g. classes/index.SDK.Foo.html)

Usage:
  py build-url-list.py
  py build-url-list.py --base-url https://www.waze.com/editor/sdk/
"""

import re
import json
import zlib
import base64
import argparse
import requests
import urllib3
from urllib.parse import urljoin
from collections import Counter

# Corporate proxy SSL inspection -- suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_BASE_URL = "https://beta.waze.com/editor/sdk/"


def make_session():
    s = requests.Session()
    s.headers["User-Agent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    return s


def fetch(url, session):
    resp = session.get(url, timeout=30, verify=False)
    resp.raise_for_status()
    return resp.text


def decode_typedoc_data(js_text, var_name):
    """
    Decode a TypeDoc compressed data variable.
    Format: window.<var_name> = "<base64(zlib(JSON))>"
    Returns parsed Python object, or None if not found.
    """
    pattern = re.compile(
        r'window\.' + re.escape(var_name) + r'\s*=\s*"([^"]+)"'
    )
    m = pattern.search(js_text)
    if not m:
        return None
    try:
        raw = zlib.decompress(base64.b64decode(m.group(1)))
        return json.loads(raw)
    except Exception as e:
        print(f"  [warn] Could not decode {var_name}: {e}")
        return None


def walk_nav_tree(node, paths):
    """Recursively walk the navigationData tree, collecting all 'path' values."""
    if isinstance(node, dict):
        if "path" in node and node["path"]:
            paths.add(node["path"])
        for child in node.get("children", []):
            walk_nav_tree(child, paths)
    elif isinstance(node, list):
        for item in node:
            walk_nav_tree(item, paths)


def sort_key(path):
    parts = path.split("/")
    if len(parts) == 1:
        return (0, path)
    return (1, parts[0], parts[1])


def main():
    parser = argparse.ArgumentParser(
        description="Build Waze SDK URL list from TypeDoc SPA navigation bundle"
    )
    parser.add_argument(
        "--base-url", default=DEFAULT_BASE_URL,
        help=f"Base URL of the SDK docs site (default: {DEFAULT_BASE_URL})"
    )
    parser.add_argument(
        "--out", default="url-list.txt",
        help="Output file for full URLs (default: url-list.txt)"
    )
    parser.add_argument(
        "--out-paths", default="url-list-paths.txt",
        help="Output file for relative paths (default: url-list-paths.txt)"
    )
    args = parser.parse_args()

    base_url = args.base_url
    if not base_url.endswith("/"):
        base_url += "/"

    session = make_session()
    all_paths = set()

    # ── Step 1: navigationData (primary source -- full sidebar tree) ──────────
    nav_url = urljoin(base_url, "assets/navigation.js")
    print(f"[1] Fetching {nav_url}")
    nav_js = fetch(nav_url, session)
    nav_data = decode_typedoc_data(nav_js, "navigationData")
    if nav_data:
        walk_nav_tree(nav_data, all_paths)
        print(f"    navigationData: {len(all_paths)} paths found")
    else:
        print("    [warn] navigationData not found or could not be decoded")

    # ── Step 2: searchData (secondary -- catches any pages not in nav tree) ──
    search_url = urljoin(base_url, "assets/search.js")
    print(f"[2] Fetching {search_url}")
    search_js = fetch(search_url, session)
    search_data = decode_typedoc_data(search_js, "searchData")
    before = len(all_paths)
    if search_data:
        rows = search_data if isinstance(search_data, list) else search_data.get("rows", [])
        for row in rows:
            if isinstance(row, dict) and row.get("url"):
                all_paths.add(row["url"].split("#")[0])  # strip anchor
        added = len(all_paths) - before
        print(f"    searchData: {added} additional paths added")
    else:
        print("    [warn] searchData not found or could not be decoded")

    # ── Step 3: always include top-level pages ────────────────────────────────
    for page in ("index.html", "modules.html"):
        all_paths.add(page)

    # ── Output ────────────────────────────────────────────────────────────────
    sorted_paths = sorted(all_paths, key=sort_key)
    full_urls = [urljoin(base_url, p) for p in sorted_paths]

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(full_urls) + "\n")

    with open(args.out_paths, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted_paths) + "\n")

    print(f"\n[3] Done! {len(sorted_paths)} URLs total.")
    print(f"    Full URLs  -> {args.out}")
    print(f"    Rel paths  -> {args.out_paths}")
    print()

    cats = Counter(p.split("/")[0] if "/" in p else "(top-level)" for p in sorted_paths)
    print("  Breakdown:")
    for cat, count in sorted(cats.items()):
        print(f"    {cat:<20s} {count:4d}")


if __name__ == "__main__":
    main()
