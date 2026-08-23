#!/usr/bin/env python3
"""Write remaining static HTML pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

HEADER = '''    <a class="skip" href="#content">Skip to content</a>
    <header class="site-header">
      <div class="wrap">
        <a class="brand" href="/">
          <img class="brand-mark" src="/assets/images/logo.svg" alt="">
          <span class="brand-text">
            <strong>WIRED</strong>
            <span>Underwater Robotics</span>
          </span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">☰</button>
        <nav class="nav" id="site-nav">
          <a href="/">Home</a>
          <a href="/vehicles/">Vehicles</a>
          <a href="/team/">Team</a>
          <a href="/gallery/">Gallery</a>
          <a href="/achievements/">Achievements</a>
          <a href="/join/">Join</a>
          <a href="/faq/">FAQ</a>
          <a href="/sponsors/">Sponsors</a>
          <a href="/contact/">Contact</a>
        </nav>
      </div>
    </header>
'''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="/assets/images/logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
''' + HEADER + '''  <main id="content">
'''

FOOT = '''
  </main>
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <h3>WIRED AUV</h3>
        <p>Women in Robotics, Engineering &amp; Development<br>Texas A&amp;M University · College Station, TX</p>
        <p><a href="mailto:reaf.tamu@gmail.com">reaf.tamu@gmail.com</a></p>
      </div>
      <div>
        <h3>Explore</h3>
        <p><a href="/vehicles/">Vehicles</a><br>
        <a href="/team/">Meet the team</a><br>
        <a href="/join/">Join the team</a><br>
        <a href="/faq/">FAQ</a></p>
      </div>
      <div>
        <h3>Follow</h3>
        <p><a href="https://www.instagram.com/wired.auv/" target="_blank" rel="noreferrer">Instagram</a><br>
        <a href="https://www.facebook.com/WEREAFTAMU/" target="_blank" rel="noreferrer">Facebook</a><br>
        <a href="https://robosub.org/" target="_blank" rel="noreferrer">RoboSub</a></p>
      </div>
    </div>
    <div class="wrap legal">© 2026 TAMU WIRED Underwater Robotics. Formerly REAF / WE REAF.</div>
  </footer>
  <script src="/assets/js/site.js"></script>
</body>
</html>
'''


def write(rel: str, title: str, description: str, body: str, hero_img: str | None = None) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    hero = ""
    if hero_img:
        hero = f'''    <section class="page-hero" style="background-image:linear-gradient(180deg,rgba(6,16,24,.45),rgba(6,16,24,.82)),url('{hero_img}')">
      <div class="wrap">
        <p class="kicker">WIRED AUV</p>
        <h1>{title.split("|")[0].strip()}</h1>
        <p>{description}</p>
      </div>
    </section>
'''
    path.write_text(HEAD.format(title=title, description=description) + hero + body + FOOT, encoding="utf-8")
    print("wrote", path)


def main() -> None:
    write(
        "join/index.html",
        "Join the Team | WIRED AUV",
        "Join WIRED Underwater Robotics at any point in the school year. No experience required.",
        '''
    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">2025–2026</p>
          <h2>We want you on the team.</h2>
          <p class="intro">Fill out the interest form, then show up to meetings. You can join at any point in the school year. Membership is open to all undergraduate engineering students.</p>
          <div class="actions">
            <a class="btn btn-primary" href="https://forms.gle/WBBvUqD1bYdxJKo56" target="_blank" rel="noreferrer">Interest form</a>
            <a class="btn btn-outline" href="/faq/">Read the FAQ</a>
          </div>
          <ul class="meet-times" style="margin-top:32px;color:var(--ink)">
            <li><strong>Programming</strong><span>Tuesdays, 6–7 PM · Zach 282D</span></li>
            <li><strong>Electrical</strong><span>Thursdays, 7:30–8:30 PM · Zach 282K</span></li>
            <li><strong>Mechanical</strong><span>Thursdays, 7–9 PM · Zach 250 or FEDC</span></li>
          </ul>
          <p style="color:var(--muted)">Locations vary. Email <a href="mailto:reaf.tamu@gmail.com">reaf.tamu@gmail.com</a> to get added to Discord.</p>
        </div>
        <div class="frame">
          <img src="/assets/images/hero-team.jpg" alt="WIRED AUV team at RoboSub">
        </div>
      </div>
    </section>
''',
        "/assets/images/hero-team.jpg",
    )

    write(
        "faq/index.html",
        "FAQ | WIRED AUV",
        "Common questions about joining WIRED Underwater Robotics at Texas A&M.",
        '''
    <section class="section">
      <div class="wrap split">
        <div class="faq">
          <details open>
            <summary>Do I need experience to join?</summary>
            <p>No. Members of all experience levels are welcome.</p>
          </details>
          <details>
            <summary>What is the time commitment?</summary>
            <p>About three hours per week: two in a subteam meeting and one in a general meeting. Members can join more than one subteam.</p>
          </details>
          <details>
            <summary>What opportunities does this team bring?</summary>
            <p>Connections to industry, technical experience, mentorship, and a support system — plus a competition vehicle you helped build.</p>
          </details>
          <details>
            <summary>Can graduate students join?</summary>
            <p>Typically graduate students mentor from the outside. Membership can be reviewed case by case.</p>
          </details>
          <details>
            <summary>How do I join?</summary>
            <p>Show up to meetings. Times are listed on the home and join pages. More information is sent through Discord. Email reaf.tamu@gmail.com to be added.</p>
          </details>
          <div class="actions" style="margin-top:24px">
            <a class="btn btn-primary" href="/contact/">More questions? Contact us</a>
          </div>
        </div>
        <div class="frame">
          <img src="/assets/images/faq-photo.jpg" alt="Team working in the lab">
        </div>
      </div>
    </section>
''',
        "/assets/images/faq-photo.jpg",
    )

    write(
        "contact/index.html",
        "Contact | WIRED AUV",
        "Reach WIRED Underwater Robotics at reaf.tamu@gmail.com.",
        '''
    <section class="section">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Get in touch</p>
          <h2>We would love to hear from you.</h2>
          <p class="intro">Recruiting, sponsorship, media, or just curiosity — email the team or use the form. It opens a message to <a href="mailto:reaf.tamu@gmail.com">reaf.tamu@gmail.com</a>.</p>
          <form class="stack" id="contact-form">
            <label><span>Name</span><input name="name" required></label>
            <label><span>Email</span><input type="email" name="email" required></label>
            <label><span>Message</span><textarea name="message" required></textarea></label>
            <button class="btn btn-primary" type="submit">Send message</button>
          </form>
        </div>
        <div class="frame tall">
          <img src="/assets/images/contact-photo.jpg" alt="WIRED AUV members">
        </div>
      </div>
    </section>
''',
        "/assets/images/contact-photo.jpg",
    )

    write(
        "sponsors/index.html",
        "Sponsors | WIRED AUV",
        "Thank you to the companies and college partners who support WIRED Underwater Robotics.",
        '''
    <section class="section">
      <div class="wrap">
        <p class="intro">Sponsorship keeps batteries charged, hulls watertight, and students at competition. Interested in supporting the team? <a href="/contact/" style="color:var(--maroon);font-weight:600">Contact us</a>.</p>
        <div class="sponsor-grid" style="margin-top:36px">
          <a class="sponsor" href="https://www.blueorigin.com/" target="_blank" rel="noreferrer"><img src="/assets/images/sponsor-williams.jpg" alt="Williams Companies / Blue Origin"></a>
          <a class="sponsor" href="https://www.caterpillar.com/en.html" target="_blank" rel="noreferrer"><img src="/assets/images/sponsor-psx.png" alt="Phillips 66"></a>
          <div class="sponsor"><img src="/assets/images/sponsor-chevron.png" alt="Chevron"></div>
          <a class="sponsor" href="https://www.l3harris.com/" target="_blank" rel="noreferrer"><img src="/assets/images/sponsor-l3harris.jpg" alt="L3Harris"></a>
          <a class="sponsor" href="https://www.bp.com/" target="_blank" rel="noreferrer"><img src="/assets/images/sponsor-trp.png" alt="BP"></a>
          <a class="sponsor" href="https://engineering.tamu.edu/" target="_blank" rel="noreferrer"><img src="/assets/images/sponsor-tamu-coe.png" alt="Texas A&amp;M College of Engineering"></a>
          <div class="sponsor"><img src="/assets/images/sponsor-tektronix.png" alt="Tektronix"></div>
        </div>
      </div>
    </section>
''',
        "/assets/images/about-team.jpg",
    )

    write(
        "gallery/index.html",
        "Gallery | WIRED AUV",
        "Photos from the lab, the pool, and RoboSub.",
        '''
    <section class="section">
      <div class="wrap">
        <div class="vehicle-grid">
          <a class="vehicle-card" href="/gallery/2024-2025/">
            <img src="/assets/images/gallery-2024.jpg" alt="2024-2025 gallery">
            <div class="inner"><div class="year">Season</div><h3>2024–2025</h3></div>
          </a>
          <a class="vehicle-card" href="/gallery/2023-2024/">
            <img src="/assets/images/gallery-2023.jpg" alt="2023-2024 gallery">
            <div class="inner"><div class="year">Season</div><h3>2023–2024</h3></div>
          </a>
          <a class="vehicle-card" href="/gallery/2022-2023/">
            <img src="/assets/images/gallery-2022.jpg" alt="2022-2023 gallery">
            <div class="inner"><div class="year">Season</div><h3>2022–2023</h3></div>
          </a>
          <a class="vehicle-card" href="/gallery/2021-2022/">
            <img src="/assets/images/gallery-2021.jpg" alt="2021-2022 gallery">
            <div class="inner"><div class="year">Season</div><h3>2021–2022</h3></div>
          </a>
          <a class="vehicle-card" href="/gallery/2020-2021/">
            <img src="/assets/images/gallery-2020.jpg" alt="2020-2021 gallery">
            <div class="inner"><div class="year">Season</div><h3>2020–2021</h3></div>
          </a>
          <a class="vehicle-card" href="/gallery/2019-2020/">
            <img src="/assets/images/gallery-2019.jpg" alt="2019-2020 gallery">
            <div class="inner"><div class="year">Season</div><h3>2019–2020</h3></div>
          </a>
        </div>
      </div>
    </section>
''',
        "/assets/images/gallery-2024.jpg",
    )

    write(
        "achievements/index.html",
        "Achievements | WIRED AUV",
        "Competition results, outreach, and campus showcases.",
        '''
    <section class="section">
      <div class="wrap achieve-list">
        <article class="achieve">
          <img src="/assets/images/vehicle-ditto-3.jpg" alt="Team at RoboSub">
          <div class="copy">
            <time>August 6, 2023</time>
            <h2>RoboSub 2023 semifinalists</h2>
            <p>Eleven engineering students from Texas A&amp;M competed against 33 other teams in San Diego. A year of work paid off: the team reached the semifinals.</p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-ray-iii.jpg" alt="Ray III at competition">
          <div class="copy">
            <time>August 2, 2022</time>
            <h2>Brightest Spark of Curiosity — RoboSub 2021</h2>
            <p>The team was recognized for asking questions and learning from peers: how other teams were structured, and the ins and outs of their AUVs.</p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-minnow.jpg" alt="Minnow era team">
          <div class="copy">
            <time>August 4, 2019</time>
            <h2>2nd place video, RoboSub 2019</h2>
            <p>A vampire-themed movie trailer introduced the team. They finished one point from first.</p>
            <p><a class="btn btn-outline" href="https://youtu.be/DbI6oLOKncg" target="_blank" rel="noreferrer">Watch the video</a></p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/achieve-girlscouts.jpg" alt="Girl Scouts STEM outreach">
          <div class="copy">
            <time>May 5, 2018</time>
            <h2>Women in Engineering program for Girl Scouts</h2>
            <p>WE REAF traveled to the STEM center grand opening in Dallas to talk with Girl Scouts about the AUV team and opportunities for women in STEM.</p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-nessie-2.jpg" alt="Nessie on display">
          <div class="copy">
            <time>May 1, 2018</time>
            <h2>Engineering Project Showcase</h2>
            <p>WE REAF joined 200+ College of Engineering teams presenting to industry. Nessie was displayed in public for the first time.</p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-nessie.jpg" alt="Nessie">
          <div class="copy">
            <time>March 26, 2018</time>
            <h2>Student Research Week</h2>
            <p>The team presented Nessie’s specs and year-over-year improvements in poster form at the nation’s largest student-run research symposium.</p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-sharkbait.jpg" alt="Sharkbait">
          <div class="copy">
            <time>December 20, 2017</time>
            <h2>1st place, Virtual Project Showcase (non-capstone)</h2>
            <p>Among 85 teams and 300+ students, WE REAF won first in the non-capstone category.</p>
            <p><a class="btn btn-outline" href="https://www.youtube.com/watch?v=EBtB61Vb4aM" target="_blank" rel="noreferrer">Watch the video</a></p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-ula.jpg" alt="Ula Sea Jewel">
          <div class="copy">
            <time>August 6, 2017</time>
            <h2>RoboSub 2017 semifinalists</h2>
            <p>Nine engineering students supported by the Women in Engineering program competed in San Diego and reached the semifinals.</p>
            <p><a href="https://today.tamu.edu/2016/09/29/aggie-women-engineers-make-a-splash-at-international-competition/" target="_blank" rel="noreferrer">Read the Texas A&amp;M story</a></p>
          </div>
        </article>
        <article class="achieve">
          <img src="/assets/images/vehicle-sharkbait-2.jpg" alt="Early team photo">
          <div class="copy">
            <time>August 7, 2016</time>
            <h2>RoboSub 2016</h2>
            <p>Six engineering students took the first WE REAF vehicle to the international RoboSub competition in San Diego.</p>
          </div>
        </article>
      </div>
    </section>
''',
        "/assets/images/vehicle-ditto-3.jpg",
    )

    write(
        "vehicles/index.html",
        "Vehicles | WIRED AUV",
        "Every competition vehicle from Ula to Swim Shady.",
        '''
    <section class="section">
      <div class="wrap">
        <div class="vehicle-grid">
          <a class="vehicle-card" href="/vehicles/swim-shady/"><img src="/assets/images/vehicle-swim-shady.jpg" alt="Swim Shady"><div class="inner"><div class="year">2024–2025</div><h3>Swim Shady</h3></div></a>
          <a class="vehicle-card" href="/vehicles/guppy/"><img src="/assets/images/vehicle-guppy-wide.jpg" alt="Guppy"><div class="inner"><div class="year">2023–2024</div><h3>Guppy</h3></div></a>
          <a class="vehicle-card" href="/vehicles/ditto/"><img src="/assets/images/vehicle-ditto-2.png" alt="Ditto"><div class="inner"><div class="year">2022–2023</div><h3>Ditto</h3></div></a>
          <a class="vehicle-card" href="/vehicles/ray-iii/"><img src="/assets/images/vehicle-ray-iii.jpg" alt="Ray III"><div class="inner"><div class="year">2021–2022</div><h3>Ray III</h3></div></a>
          <a class="vehicle-card" href="/vehicles/ray-ii/"><img src="/assets/images/vehicle-ray-ii.jpg" alt="Ray II"><div class="inner"><div class="year">2020–2021</div><h3>Ray II</h3></div></a>
          <a class="vehicle-card" href="/vehicles/ray/"><img src="/assets/images/vehicle-ray.png" alt="Ray"><div class="inner"><div class="year">2019–2020</div><h3>Ray</h3></div></a>
          <a class="vehicle-card" href="/vehicles/minnow/"><img src="/assets/images/vehicle-minnow-2.png" alt="Minnow"><div class="inner"><div class="year">2018–2019</div><h3>Minnow</h3></div></a>
          <a class="vehicle-card" href="/vehicles/nessie/"><img src="/assets/images/vehicle-nessie-2.jpg" alt="Nessie"><div class="inner"><div class="year">2017–2018</div><h3>Nessie</h3></div></a>
          <a class="vehicle-card" href="/vehicles/sharkbait/"><img src="/assets/images/vehicle-sharkbait-2.jpg" alt="Sharkbait"><div class="inner"><div class="year">2016–2017</div><h3>Sharkbait</h3></div></a>
          <a class="vehicle-card" href="/vehicles/ula/"><img src="/assets/images/vehicle-ula.jpg" alt="Ula Sea Jewel"><div class="inner"><div class="year">2015–2016</div><h3>Ula · Sea Jewel</h3></div></a>
        </div>
      </div>
    </section>
''',
        "/assets/images/vehicle-guppy-wide.jpg",
    )


if __name__ == "__main__":
    main()
