#!/usr/bin/env python3
from pathlib import Path
from page_template import write

VEHICLES = [
    {
        "slug": "swim-shady",
        "name": "Swim Shady",
        "year": "2024–2025",
        "img": "/assets/images/vehicle-swim-shady.jpg",
        "paper": "https://docs.google.com/document/d/1yBkz5ClJ7i7JdDmjMh55Ayom3BQd5at9e2FIKcLqskk/edit?usp=sharing",
        "stats": [("Freshmen", "18"), ("Sophomores", "11"), ("Juniors", "10"), ("Seniors", "4"), ("Mechanical", "19"), ("Electrical", "14"), ("Programming", "9")],
        "body": "<p>The current-generation vehicle heading into RoboSub. CAD, hull, and thruster work continued the line from Guppy and Ditto with a tighter mechanical package.</p>",
    },
    {
        "slug": "guppy",
        "name": "Guppy",
        "year": "2023–2024",
        "img": "/assets/images/vehicle-guppy.jpg",
        "extra": "/assets/images/vehicle-guppy-wide.jpg",
        "paper": "https://docs.google.com/document/d/1jBLcY-x_o3UAGbnMoElcsQBb2sZt9310zv2B0s8964I/edit?usp=sharing",
        "stats": [("Freshmen", "18"), ("Sophomores", "12"), ("Juniors", "8"), ("Seniors", "4"), ("Mechanical", "25"), ("Electrical", "19"), ("Programming", "16")],
        "body": "<p>Guppy carried the team through the 2023–2024 season and into RoboSub. A compact, camera-forward hull with a large student roster across all three subteams.</p>",
    },
    {
        "slug": "ditto",
        "name": "Ditto",
        "year": "2022–2023",
        "img": "/assets/images/vehicle-ditto.jpg",
        "extra": "/assets/images/vehicle-ditto-3.jpg",
        "paper": "https://docs.google.com/document/d/1Hco94UwLC9Ada9BLm2BglAqEnyET7hdI019P5GuGqeo/edit?usp=sharing",
        "stats": [("Freshmen", "36"), ("Sophomores", "16"), ("Juniors", "18"), ("Seniors", "9"), ("Mechanical", "29"), ("Electrical", "27"), ("Programming", "38")],
        "body": "<p>Ditto was one of the largest teams in WIRED AUV history and reached the RoboSub 2023 semifinals in San Diego.</p>",
    },
    {
        "slug": "ray-iii",
        "name": "Ray III",
        "year": "2021–2022",
        "img": "/assets/images/vehicle-ray-iii.jpg",
        "paper": "https://docs.google.com/document/d/1dmiW2COsWlRwLmSs5mvySx3ad-iMMP3oR7KALMgybXg/edit?usp=sharing",
        "stats": [],
        "body": "<p>Third vehicle in the Ray family. The team earned RoboSub’s “Brightest Spark of Curiosity” award around this era for learning from other programs on the pool deck.</p>",
    },
    {
        "slug": "ray-ii",
        "name": "Ray II",
        "year": "2020–2021",
        "img": "/assets/images/vehicle-ray-ii.jpg",
        "paper": "https://docs.google.com/document/d/1s4hL7sbKaOzuM03G5dc7FLdMhOHc0MNjquxvibqQ9Xw/edit?usp=sharing",
        "stats": [("Freshmen", "25"), ("Sophomores", "12"), ("Juniors", "4"), ("Seniors", "1"), ("Mechanical", "35"), ("Electrical", "19"), ("Programming", "17")],
        "body": "<p>A pandemic-year iteration of Ray with a large mechanical cohort and continued sensor and hull work. CAD of the platform remains one of the team’s clearest early drawings.</p>",
    },
    {
        "slug": "ray",
        "name": "Ray",
        "year": "2019–2020",
        "img": "/assets/images/vehicle-ray.png",
        "paper": "https://docs.google.com/document/d/1s4hL7sbKaOzuM03G5dc7FLdMhOHc0MNjquxvibqQ9Xw/edit?usp=sharing",
        "paper_label": "Journal paper",
        "stats": [("Freshmen", "26"), ("Sophomores", "15"), ("Juniors", "12"), ("Seniors", "3"), ("Mechanical", "20"), ("Electrical", "15"), ("Programming", "21")],
        "body": '''
        <div class="prose">
          <h3>Mechanical</h3>
          <ul>
            <li>Trained members in SolidWorks and Fusion 360</li>
            <li>Taught manufacturing methods and how to read engineering drawings</li>
            <li>Revised structural components, including a custom-fit bottom panel</li>
            <li>New encaps for internally mounting a stereo vision camera</li>
            <li>Midcap interchangeable panels for more functionality</li>
            <li>Maneuvering arm and dropper designed for task completion</li>
          </ul>
          <h3>Electrical</h3>
          <ul>
            <li>Jetson TX2 as the main computer</li>
            <li>Fuses for ESCs and other components</li>
            <li>Custom PCB for ESC functions</li>
            <li>Upgraded watertight kill switch and mission switch</li>
            <li>Higher-voltage batteries and battery monitoring</li>
            <li>Teensy microcontroller and custom shield for sensors</li>
            <li>Hydrophone subsystem with Aquarian H2A hydrophones</li>
          </ul>
          <h3>Programming</h3>
          <ul>
            <li>Python, C++, and OpenCV onboarding</li>
            <li>ROS system integration</li>
            <li>Machine learning for object detection</li>
            <li>Image processing and motion control for competition tasks</li>
          </ul>
        </div>
        ''',
    },
    {
        "slug": "minnow",
        "name": "Minnow",
        "year": "2018–2019",
        "img": "/assets/images/vehicle-minnow.jpg",
        "extra": "/assets/images/vehicle-minnow-2.png",
        "paper": "https://robosub.org/",
        "stats": [("Freshmen", "38"), ("Sophomores", "33"), ("Juniors", "10"), ("Seniors", "7"), ("Mechatronics", "13"), ("Mechanical", "25"), ("Electrical", "19"), ("Programming", "31")],
        "body": "<p>One of the largest early rosters. Minnow’s RoboSub 2019 video placed second, one point from first, on a vampire-themed trailer.</p>",
    },
    {
        "slug": "nessie",
        "name": "Nessie",
        "year": "2017–2018",
        "img": "/assets/images/vehicle-nessie.jpg",
        "extra": "/assets/images/vehicle-nessie-2.jpg",
        "paper": "https://docs.google.com/document/d/1kEI2IQtZ6y751Sg6ZDuhz3cpy40Ex0PEpimDvX45ZMU/edit?usp=sharing",
        "stats": [("Freshmen", "11"), ("Sophomores", "6"), ("Juniors", "7"), ("Seniors", "4"), ("Mechanical", "14"), ("Electrical", "6"), ("Programming", "8")],
        "body": '''
        <div class="prose">
          <h3>Mechanical</h3>
          <ul>
            <li>Midcap for easier access and better weight and buoyancy distribution</li>
            <li>Internal lattice that keeps electronics elevated if the hull leaks</li>
            <li>More stable structure, designed for fabrication and efficient material use</li>
          </ul>
          <h3>Electrical</h3>
          <ul>
            <li>Pressure and temperature sensor integration</li>
            <li>Electronics placement for heat dissipation</li>
            <li>Computer–microcontroller communication</li>
            <li>Tether for testing and hydrophone prototyping</li>
          </ul>
          <h3>Programming</h3>
          <ul>
            <li>Faster computer vision for underwater objects</li>
            <li>Improved Intel NUC and Arduino communication for PID control</li>
            <li>AHRS yaw, pitch, and roll for movement</li>
          </ul>
        </div>
        ''',
    },
    {
        "slug": "sharkbait",
        "name": "Sharkbait",
        "year": "2016–2017",
        "img": "/assets/images/vehicle-sharkbait.jpg",
        "extra": "/assets/images/vehicle-sharkbait-2.jpg",
        "paper": "http://www.robonation.org/sites/default/files/RS17_TexasA%26MU_Paper.pdf",
        "stats": [("Freshmen", "6"), ("Sophomores", "12"), ("Juniors", "7")],
        "body": '''
        <div class="prose">
          <h3>Mechanical</h3>
          <ul>
            <li>PVC pipe hull with a polycarbonate dome</li>
            <li>Electronics prism, hollowed to run wiring</li>
            <li>Eight Blue Robotics T200 thrusters</li>
            <li>Electronic arm, two torpedo launchers, and a marble dropper</li>
            <li>Watertight hull; casings for components that were not</li>
          </ul>
          <h3>Electrical</h3>
          <ul>
            <li>Intel NUC, ATX power supply, Arduino Uno, Adafruit PWM driver, and PCB</li>
            <li>Serial commands from the NUC to thrusters and servos via Arduino</li>
            <li>VectorNav VN-100 AHRS for orientation</li>
            <li>Four 4S 10,000 mAh batteries</li>
          </ul>
          <h3>Programming</h3>
          <ul>
            <li>OpenCV for real-time object position estimates</li>
            <li>Arduino receives object and sensor data to command thrusters</li>
            <li>Software written in Python with recursive real-time control</li>
          </ul>
        </div>
        ''',
    },
    {
        "slug": "ula",
        "name": "Ula · Sea Jewel",
        "year": "2015–2016",
        "img": "/assets/images/vehicle-ula.jpg",
        "paper": "http://www.robonation.org/sites/default/files/RS17_TexasA%26MU_Paper.pdf",
        "stats": [("Freshmen", "6"), ("Sophomores", "6"), ("Juniors", "2"), ("Grad students", "1")],
        "body": '''
        <div class="prose">
          <p>The first WIRED / WE REAF competition vehicle.</p>
          <h3>Mechanical</h3>
          <ul>
            <li>Four thrusters on an outer frame</li>
            <li>Main hull with watertight endcaps for electronics</li>
            <li>Miniature hulls on top arches for batteries and camera</li>
            <li>3D-printed kill-switch housing</li>
          </ul>
          <h3>Electrical</h3>
          <ul>
            <li>Two 14.8V 10,000 mAh LiPo batteries</li>
            <li>VN-100 AHRS donated by VectorNav</li>
            <li>Two Measurement Specialties US-300 pressure sensors</li>
            <li>Two SS-Aquacam cameras</li>
            <li>Temperature sensor to protect electronics</li>
          </ul>
          <h3>Programming</h3>
          <ul>
            <li>OpenCV on camera video</li>
            <li>Two Raspberry Pi 2s for image processing and algorithms</li>
            <li>Four Arduino Unos between sensors and the Pis</li>
          </ul>
        </div>
        ''',
    },
]


def stats_html(stats):
    if not stats:
        return ""
    cells = "".join(f'<div class="spec"><b>{value}</b><span>{label}</span></div>' for label, value in stats)
    return f'<div class="spec-grid">{cells}</div>'


def extra_html(src):
    if not src:
        return ""
    return f'<div class="frame" style="margin-top:28px"><img src="{src}" alt=""></div>'


def main():
    for v in VEHICLES:
        paper = f'<a class="btn btn-outline" href="{v["paper"]}" target="_blank" rel="noreferrer">{v.get("paper_label", "Journal paper")}</a>'
        body = f'''
    <section class="section">
      <div class="wrap split">
        <div class="frame"><img src="{v["img"]}" alt="{v["name"]}"></div>
        <div>
          <p class="eyebrow">{v["year"]}</p>
          <h2>{v["name"]}</h2>
          {stats_html(v["stats"])}
          <div class="actions">{paper}<a class="btn btn-primary" href="/vehicles/">All vehicles</a></div>
        </div>
      </div>
      <div class="wrap" style="margin-top:36px">
        {v["body"]}
        {extra_html(v.get("extra"))}
      </div>
    </section>
'''
        write(
            f'vehicles/{v["slug"]}/index.html',
            f'{v["name"]} | WIRED AUV',
            f'{v["year"]} competition vehicle.',
            body,
            v["img"],
        )


if __name__ == "__main__":
    main()
