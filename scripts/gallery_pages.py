#!/usr/bin/env python3
from page_template import write

YEARS = [
    {
        "slug": "2024-2025",
        "title": "2024–2025",
        "images": [
            "gallery-2024.jpg",
            "about-team.jpg",
            "team-hero.jpg",
            "vehicle-swim-shady.jpg",
            "contact-photo.jpg",
            "faq-photo.jpg",
            "hero-team.jpg",
        ],
    },
    {
        "slug": "2023-2024",
        "title": "2023–2024",
        "images": [
            "gallery-2023.jpg",
            "vehicle-guppy.jpg",
            "vehicle-guppy-wide.jpg",
            "subteam-mechanical.jpg",
            "subteam-electrical.jpg",
            "subteam-programming.jpg",
        ],
    },
    {
        "slug": "2022-2023",
        "title": "2022–2023",
        "images": [
            "gallery-2022.jpg",
            "gallery-2022-extra.jpg",
            "vehicle-ditto.jpg",
            "vehicle-ditto-2.png",
            "vehicle-ditto-3.jpg",
        ],
    },
    {
        "slug": "2021-2022",
        "title": "2021–2022",
        "images": [
            "gallery-2021.jpg",
            "vehicle-ray-iii.jpg",
        ],
    },
    {
        "slug": "2020-2021",
        "title": "2020–2021",
        "images": [
            "gallery-2020.jpg",
            "vehicle-ray-ii.jpg",
        ],
    },
    {
        "slug": "2019-2020",
        "title": "2019–2020",
        "images": [
            "gallery-2019.jpg",
            "vehicle-ray.png",
            "vehicle-minnow.jpg",
        ],
    },
]


def main():
    for year in YEARS:
        figs = "\n".join(
            f'<figure><img src="/assets/images/{name}" alt="{year["title"]} photo"></figure>'
            for name in year["images"]
        )
        body = f'''
    <section class="section">
      <div class="wrap">
        <p><a href="/gallery/" style="color:var(--maroon);font-weight:600">← All galleries</a></p>
        <div class="lightbox-grid" style="margin-top:24px">{figs}</div>
      </div>
    </section>
'''
        write(
            f'gallery/{year["slug"]}/index.html',
            f'{year["title"]} Gallery | WIRED AUV',
            f'Photos from the {year["title"]} season.',
            body,
            f'/assets/images/{year["images"][0]}',
        )


if __name__ == "__main__":
    main()
