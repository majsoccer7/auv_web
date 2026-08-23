#!/usr/bin/env python3
"""Download original Wix media from every page on the current site."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "public" / "assets" / "images"
DOC_DIR = ROOT / "public" / "assets" / "docs"
MAP_PATH = ROOT / "scripts" / "image-map.json"

PAGES = [
    "https://reaftamu.wixsite.com/website",
    "https://reaftamu.wixsite.com/website/recruitment",
    "https://reaftamu.wixsite.com/website/faq",
    "https://reaftamu.wixsite.com/website/sponsors",
    "https://reaftamu.wixsite.com/website/contact",
    "https://reaftamu.wixsite.com/website/meet-the-team",
    "https://reaftamu.wixsite.com/website/copy-of-meet-the-team",
    "https://reaftamu.wixsite.com/website/copy-of-2023-2024-guppy",
    "https://reaftamu.wixsite.com/website/copy-of-2022-2023-ditto",
    "https://reaftamu.wixsite.com/website/blank",
    "https://reaftamu.wixsite.com/website/copy-of-2020-2021-ray-ii",
    "https://reaftamu.wixsite.com/website/copy-of-2019-2020-ray",
    "https://reaftamu.wixsite.com/website/2019-2020-ray",
    "https://reaftamu.wixsite.com/website/2018-2019-minnow",
    "https://reaftamu.wixsite.com/website/copy-of-2016-2017",
    "https://reaftamu.wixsite.com/website/copy-of-2015-2016",
    "https://reaftamu.wixsite.com/website/2015-2016",
    "https://reaftamu.wixsite.com/website/our-past",
    "https://reaftamu.wixsite.com/website/news",
    "https://reaftamu.wixsite.com/website/copy-of-2023-2024",
    "https://reaftamu.wixsite.com/website/copy-of-2022-2023",
    "https://reaftamu.wixsite.com/website/copy-of-2019-2020-1",
    "https://reaftamu.wixsite.com/website/copy-of-2019-2020",
    "https://reaftamu.wixsite.com/website/2019-2020",
    "https://reaftamu.wixsite.com/website/achievements",
    "https://reaftamu.wixsite.com/website/more",
]

DOCS = [
    (
        "https://5bd697cd-836b-4431-b262-ea33d2bd7818.filesusr.com/ugd/a3572c_1092c197df2c4fc28550c17590d5c340.pdf",
        "minnow-2018-2019.pdf",
    ),
    (
        "https://5bd697cd-836b-4431-b262-ea33d2bd7818.filesusr.com/ugd/a3572c_4b29eb4116df4dffafba7de12a04b561.pdf",
        "ray-2019-2020.pdf",
    ),
]

SKIP_PREFIXES = (
    "11062b_",
    "nsplsh_",
    "11062b",
)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def original_url(media_id: str) -> str:
    return f"https://static.wixstatic.com/media/{media_id}"


def collect_media_ids(html: str) -> set[str]:
    ids: set[str] = set()
    for match in re.finditer(
        r"static\.wixstatic\.com/media/([A-Za-z0-9_\-.%~]+?\.(?:jpg|jpeg|png|gif|webp|avif|JPG|JPEG|PNG|HEIC))",
        html,
    ):
        ids.add(match.group(1).split("/")[0])
    for match in re.finditer(
        r'"(?:uri|url|fileName)"\s*:\s*"((?:a3572c|11062b)_[^"]+\.(?:jpg|jpeg|png|gif|webp))"',
        html,
        flags=re.I,
    ):
        ids.add(match.group(1))
    for match in re.finditer(
        r"(a3572c_[a-f0-9]{32}(?:~mv2(?:_d_\d+_\d+_s_\d(?:_\d)?)?)?\.(?:jpg|jpeg|png|gif|webp))",
        html,
        flags=re.I,
    ):
        ids.add(match.group(1))
    return ids


def should_skip(media_id: str) -> bool:
    lowered = media_id.lower()
    if lowered.startswith(SKIP_PREFIXES):
        return True
    if "wix" in lowered and "logo" in lowered:
        return True
    return False


def download_file(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1024:
        return True
    try:
        data = fetch(url)
        if len(data) < 200:
            return False
        dest.write_bytes(data)
        return True
    except urllib.error.HTTPError as exc:
        print(f"  FAIL {exc.code} {url}")
        return False
    except Exception as exc:  # noqa: BLE001
        print(f"  ERR  {exc} {url}")
        return False


def main() -> None:
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    DOC_DIR.mkdir(parents=True, exist_ok=True)
    all_ids: set[str] = set()
    page_map: dict[str, list[str]] = {}

    for page in PAGES:
        print(f"SCAN {page}")
        try:
            html = fetch(page).decode("utf-8", errors="ignore")
        except Exception as exc:  # noqa: BLE001
            print(f"  skip page: {exc}")
            continue
        ids = {i for i in collect_media_ids(html) if not should_skip(i)}
        page_map[page] = sorted(ids)
        all_ids.update(ids)
        print(f"  found {len(ids)} media ids")
        time.sleep(0.2)

    mapping: dict[str, str] = {}
    for media_id in sorted(all_ids):
        filename = media_id.replace("%20", "_").replace(" ", "_")
        dest = IMG_DIR / filename
        url = original_url(media_id)
        print(f"GET  {filename}")
        if download_file(url, dest):
            mapping[media_id] = f"assets/images/{filename}"
        time.sleep(0.05)

    for url, name in DOCS:
        print(f"DOC  {name}")
        download_file(url, DOC_DIR / name)

    MAP_PATH.write_text(json.dumps({"pages": page_map, "files": mapping}, indent=2), encoding="utf-8")
    print(f"\nDownloaded {len(mapping)} images to {IMG_DIR}")


if __name__ == "__main__":
    main()
