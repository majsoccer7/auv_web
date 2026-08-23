#!/usr/bin/env python3
"""Retry 403 original downloads via Wix fill URLs, and copy friendly names."""

from __future__ import annotations

import json
import shutil
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "public" / "assets" / "images"
DOC = ROOT / "public" / "assets" / "docs"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

FAILED = [
    "a3572c_049b7a6436604573a8fe82b9d002d184~mv2.png",
    "a3572c_04d7a9e32a8148eba463b232635dc34d~mv2_d_4000_6000_s_4_2.jpg",
    "a3572c_1810b63233e742fabbe712027575ce0c~mv2.jpg",
    "a3572c_1a440930a2e9417192c688913e09cfdc~mv2.jpeg",
    "a3572c_1c266fa3dd0d4202b5dcc5a39adfe9ba~mv2_d_4096_2730_s_4_2.jpg",
    "a3572c_1d83587cc30941e9a10da09bdd4e959e~mv2.png",
    "a3572c_1e849a3c77d54d0cb5da76706449aed0~mv2.jpg",
    "a3572c_228c8e2db16f490f921514f1655241b5~mv2_d_1800_1200_s_2.jpg",
    "a3572c_278d02fe99ee4709ac21e4f02c16649d~mv2.jpg",
    "a3572c_2b4eb66bd7c045c4a319e112e73f8baa~mv2.jpg",
    "a3572c_3233758761e444b39e474f5af4797590~mv2.jpg",
    "a3572c_34d90326ba8a4151aee25bc931d6331f~mv2.jpg",
    "a3572c_36e989500f0a455b885beae668ee9274~mv2_d_3000_2000_s_2.jpg",
    "a3572c_410b709608a144d98cd0732bba0b1787~mv2.jpg",
    "a3572c_4b104bd0051742229cf68a790e0c55d5~mv2_d_1800_1200_s_2.jpg",
    "a3572c_59fcd5bf93984432a0d190959fe7a011~mv2_d_3024_4032_s_4_2.jpg",
    "a3572c_6003c09452f7410385846b13e9f6b106~mv2.jpg",
    "a3572c_6b8c14456b484b99ac58758cbf015a11~mv2.jpg",
    "a3572c_788b64d311244b0d94e4883dddcf660f~mv2.jpg",
    "a3572c_7ce7383ed10b49e9bbc2e9384c6367e7~mv2.png",
    "a3572c_8146e1d688fa4e389ef02aaf4433e600~mv2_d_4608_3456_s_4_2.jpg",
    "a3572c_866cf14174b04590a6a79fe0240f4b6b~mv2.jpg",
    "a3572c_896977b8b314418bb08f30faeecbaf23~mv2.jpg",
    "a3572c_8adc9d1a6b17434a8eff5629d4aacdd5~mv2.jpg",
    "a3572c_8cfbf5cfed784b7c8469272043145825~mv2.jpg",
    "a3572c_8ff716df121346e799411cb3d71faff3~mv2.jpg",
    "a3572c_ac1872be7dba4be99e496c00de3f1001~mv2.jpg",
    "a3572c_b613de3993ce458f88be918298a4c12e~mv2.jpg",
    "a3572c_c0ff7553e8c44c5e9b9c17f3c3761c42~mv2_d_6000_4000_s_4_2.jpg",
    "a3572c_ceb1c029330c4e87b581e4403ad77d62~mv2.jpg",
    "a3572c_d620af30ed1440948a6c324b26ad0948~mv2.png",
    "a3572c_e2bbc16797d94e929a656330d738da97~mv2.png",
    "a3572c_e7571da2debb472ea6b5b728badfa4be~mv2.jpg",
    "a3572c_eb1acad880f8439c98cf5ca3eef0cd13~mv2.png",
    "a3572c_f0aaeeef33234833b5c967ebc2ba5ae7~mv2.png",
    "a3572c_fc95eb1cca6f4435bf8d379c78256bbf~mv2.jpg",
]

FRIENDLY = {
    "hero-team.jpg": "a3572c_f3f4527d5e8a45ef824f7d6c0e3fe49f~mv2.jpg",
    "about-team.jpg": "a3572c_6772c205b0424f0682bce13a6b2956e0~mv2.jpg",
    "subteam-mechanical.jpg": "a3572c_1d8677ac95874b1dbd58852692d62096~mv2.jpg",
    "subteam-electrical.jpg": "a3572c_f21616053dee4dadbb94544b7e3c2aa5~mv2.jpg",
    "subteam-programming.jpg": "a3572c_7095236afcce4f5c8e33b01415294ebb~mv2.jpg",
    "logo-photo.jpg": "a3572c_ec7333a04ad142ae8560e16f26ff984c~mv2.jpg",
    "join-hero.png": "a3572c_951695a6f5194604b7261ccd764a6258~mv2.png",
    "faq-photo.jpg": "a3572c_c63a9f7dda6a4397b0b6aa2f74e7087f~mv2.jpg",
    "contact-photo.jpg": "a3572c_dfb98ac529bd40159566de7fe3307104~mv2.jpg",
    "team-hero.jpg": "a3572c_a8249f1872da4caf8a40f5b120718ded~mv2.jpg",
    "sponsor-williams.jpg": "a3572c_bd59349732af47aaafa74fbc62f20ccf~mv2.jpg",
    "sponsor-psx.png": "a3572c_03ed7c45aa9d4867a1e922424a79c91e~mv2.png",
    "sponsor-chevron.png": "a3572c_c48dd73326f14b2cb3bc9a3b3770824b~mv2.png",
    "sponsor-l3harris.jpg": "a3572c_c74c6d1c4f9341739a1096ac4bd8d7a7~mv2.jpg",
    "sponsor-tamu-coe.png": "a3572c_5233f7835e884c49920a007c2fc353ef~mv2.png",
    "sponsor-trp.png": "a3572c_72e0dbe2984641c887aa52370a7b8e9a~mv2.png",
    "sponsor-tektronix.png": "a3572c_7274ce84d4184d3d8aad2ab8e0e9a2dc~mv2.png",
    "vehicle-swim-shady.jpg": "a3572c_b1fad6a6b63e40428b2a71ec4b71371b~mv2.jpg",
    "vehicle-guppy.jpg": "a3572c_e30474a1311e43588189322ce3ce0d0c~mv2.jpg",
    "vehicle-guppy-wide.jpg": "a3572c_500a50027f8b4f2083c34e8b85c062fb~mv2.jpg",
    "vehicle-ditto.jpg": "a3572c_42ae103f232d4d76913ed917574a3015~mv2.jpg",
    "vehicle-ditto-2.png": "a3572c_4414ddb5ddc74bb39f4aac2f915007c2~mv2.png",
    "vehicle-ditto-3.jpg": "a3572c_48bf3f7db1764eddb973894b1c51e229~mv2.jpg",
    "vehicle-ray-iii.jpg": "a3572c_4abffc1d80a7463db5b591fbde88d995~mv2.jpg",
    "vehicle-ray-ii.jpg": "a3572c_5a1e4050be9e421bb2515396ba255650~mv2.jpg",
    "vehicle-ray.png": "a3572c_f94bba97ec524507ba10ab24e75f72aa~mv2.png",
    "vehicle-minnow.jpg": "a3572c_a3085560c71f4fb4800ae4dee2c91707~mv2.jpg",
    "vehicle-minnow-2.png": "a3572c_2ec95a5aefe64092a9b0f5276cc17177~mv2.png",
    "vehicle-nessie.jpg": "a3572c_2487c756ae6c4898bda916891faf3ce6~mv2.jpg",
    "vehicle-nessie-2.jpg": "a3572c_235a3b98574b43bf9fbb8d0600de13db~mv2.jpg",
    "vehicle-sharkbait.jpg": "a3572c_118f603008f9461680bd07bfa2baba51~mv2.jpg",
    "vehicle-sharkbait-2.jpg": "a3572c_9d790eb73ecf4387b47286fd758cb073~mv2.jpg",
    "vehicle-ula.jpg": "a3572c_61bf896c48544dec89d5de91ee8c0f62~mv2.jpg",
    "gallery-2024.jpg": "a3572c_677c00b56f994c49a352a3437e8765ea~mv2.jpg",
    "gallery-2023.jpg": "a3572c_7b87c37e470c44f8a0afc2d00fc46e5a~mv2.jpg",
    "gallery-2022.jpg": "a3572c_381e662050284a82a55c70958cf2ee0e~mv2.jpg",
    "gallery-2021.jpg": "a3572c_edb5134458654963bd17950ca8e209aa~mv2.jpg",
    "gallery-2020.jpg": "a3572c_ee7c6f5fd0724729a30b50accbb42b02~mv2.jpg",
    "gallery-2019.jpg": "a3572c_d1c5d40876f74060ae2d56dbc0dabd2d~mv2.jpg",
    "gallery-2022-extra.jpg": "a3572c_5de196eb737044139e7cfa6fa7a04d51f000.jpg",
    "achieve-girlscouts.jpg": "a3572c_8bfc102f195a46c9b59bb73adda4ad99~mv2.jpg",
    "waves.jpg": "40c2397700984377a8d5a841d6b818ef.jpg",
}


def fetch(url: str, referer: str | None = None) -> bytes:
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def try_download(media_id: str) -> bool:
    dest = IMG / media_id
    if dest.exists() and dest.stat().st_size > 1024:
        return True
    candidates = [
        f"https://static.wixstatic.com/media/{media_id}/v1/fill/w_1600,h_1600,al_c,q_90,enc_auto/{media_id}",
        f"https://static.wixstatic.com/media/{media_id}/v1/fill/w_1200,h_800,al_c,q_85,usm_0.66_1.00_0.01/{media_id}",
        f"https://static.wixstatic.com/media/{media_id}/v1/fit/w_1200,h_1200,al_c,q_85/{media_id}",
    ]
    for url in candidates:
        try:
            data = fetch(url, referer="https://reaftamu.wixsite.com/")
            if len(data) > 400:
                dest.write_bytes(data)
                print(f"OK   {media_id} ({len(data)} bytes)")
                return True
        except urllib.error.HTTPError as exc:
            print(f"  {exc.code} {url}")
        except Exception as exc:  # noqa: BLE001
            print(f"  err {exc}")
    print(f"FAIL {media_id}")
    return False


def copy_friendly() -> None:
    for dest_name, src_name in FRIENDLY.items():
        src = IMG / src_name
        dest = IMG / dest_name
        if src.exists():
            shutil.copyfile(src, dest)
            print(f"COPY {dest_name}")
        else:
            print(f"MISS {src_name} -> {dest_name}")


def retry_docs() -> None:
    DOC.mkdir(parents=True, exist_ok=True)
    docs = [
        (
            "https://5bd697cd-836b-4431-b262-ea33d2bd7818.filesusr.com/ugd/a3572c_1092c197df2c4fc28550c17590d5c340.pdf",
            "minnow-2018-2019.pdf",
        ),
        (
            "https://5bd697cd-836b-4431-b262-ea33d2bd7818.filesusr.com/ugd/a3572c_4b29eb4116df4dffafba7de12a04b561.pdf",
            "ray-2019-2020.pdf",
        ),
    ]
    for url, name in docs:
        dest = DOC / name
        try:
            data = fetch(url, referer="https://reaftamu.wixsite.com/")
            dest.write_bytes(data)
            print(f"DOC  {name} ({len(data)})")
        except Exception as exc:  # noqa: BLE001
            print(f"DOC FAIL {name}: {exc}")


def main() -> None:
    for media_id in FAILED:
        try_download(media_id)
    copy_friendly()
    retry_docs()
    (ROOT / "scripts" / "friendly-map.json").write_text(json.dumps(FRIENDLY, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
