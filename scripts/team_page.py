#!/usr/bin/env python3
from page_template import write

IMG = "/assets/images/"

OFFICERS = [
    ("Rishika Desai", "Team Captain", "a3572c_64827748fcb94a1e8643e7db4e0b3405~mv2.jpg"),
    ("Azhure Landers", "Project Manager", "a3572c_9ce8928832c444e290f05dbb4462f873~mv2.jpg"),
    ("Nisha Murali", "Vice Captain", "a3572c_b64290cda84d4738ac0e066f99cbf034~mv2.jpg"),
    ("Parvathi Menon", "Vice Project Manager", "a3572c_fcbd2e0c2f7f4e38b2142d73b07b836a~mv2.jpg"),
    ("Asmita Subash", "Mechanical Lead", "a3572c_2c2284e570eb4a9dbb1476a21b48ef6e~mv2.png"),
    ("Adithi Iyer Ganesan", "Mechanical Sub-Lead", "a3572c_1ab9f64f85e945db886ad9e1f9f096d0~mv2.jpg"),
    ("Brooklyn Simpson", "Manufacturing Lead", "a3572c_5525bd80007b4b599204c6b352880efa~mv2.jpg"),
    ("Sanjana Anand", "Programming Co-Lead", "a3572c_be45fa69107e4c36b91e25ae185f2a2f~mv2.jpg"),
    ("Tanvi Kangralkar", "Programming Co-Lead", "a3572c_82a7132bcea5431baf1f3e1a109a6772~mv2.jpg"),
    ("Alex Holmes", "Programming Mentor", "a3572c_73bf0d36e8074b639f8a3b7580d4ee5a~mv2.jpg"),
    ("Raquel Susko", "Electrical Lead", "a3572c_83452cf2ccd24073b8ad3f5896d84486~mv2.jpg"),
    ("Tanvi Naragoni", "Electrical Sub-Lead", "a3572c_fbcbac0559864daa80e49b2258d55056~mv2.jpg"),
    ("Adiba Mahjabeen", "Electrical Mentor", "a3572c_696c96bf37a14c569580ac516ff263cc~mv2.png"),
    ("Daneli Estrada", "Social Media Officer", "a3572c_64414b4b819b4a0eb4fc829d316609ff~mv2.png"),
    ("Ana Cruz", "Secretary", "a3572c_41bae85ab42f41ddb39c32cc33aa7bfd~mv2.jpg"),
]

MECH = [
    ("Daneli Estrada", "a3572c_64414b4b819b4a0eb4fc829d316609ff~mv2.png"),
    ("Riley Arnett", "a3572c_963f0ce59d844af5a114e381ba24fc0e~mv2.png"),
    ("Andrea Simon", "a3572c_b749da7e5709446f93928a9a9b1edbdf~mv2.png"),
    ("Grace Awalt", "a3572c_a86b27b81e09458e9226ba11f16d7d6e~mv2.png"),
    ("Aarathi Devakumar", "a3572c_61535b4d24934826af912b8586dc005b~mv2.png"),
    ("Anna Miley", "a3572c_b5cb842e00df4433a8f0467bdabd4654~mv2.jpg"),
    ("Adithi Iyer Ganesan", "a3572c_1ab9f64f85e945db886ad9e1f9f096d0~mv2.jpg"),
    ("Rishika Desai", "a3572c_93f4d84615b64096ad42c8511835739f~mv2.jpg"),
    ("Katie Querrey", "a3572c_9167ffa4903e4a0f95309d883e565258~mv2.jpeg"),
    ("Azhure Landers", "a3572c_9ce8928832c444e290f05dbb4462f873~mv2.jpg"),
    ("Mihika Varshney", "a3572c_3b44cf67ef2745aaa5a998f65dbfcdd0~mv2.jpg"),
    ("Emma Stewart", "a3572c_9f764bc228f344d7b3af0bba0581ca5b~mv2.jpg"),
    ("Asmita Subash", "a3572c_2c2284e570eb4a9dbb1476a21b48ef6e~mv2.png"),
    ("Brooklyn Simpson", "a3572c_5525bd80007b4b599204c6b352880efa~mv2.jpg"),
    ("Mehek Patro", "a3572c_90b820f34c6b4c5daadb8ccdc42cd477~mv2.jpeg"),
    ("Leslie Benitez", "a3572c_1066e0a27467446f96dceab3c57b9455~mv2.jpg"),
    ("Elsa Kurji", "a3572c_3eac54c873b74570be0e53ebc05cf9c9~mv2.jpeg"),
    ("Jaanvi Patel", "a3572c_f1a13bb8215f40e185ed0bc2a0824ba4~mv2.jpg"),
    ("Ana Cruz", "a3572c_41bae85ab42f41ddb39c32cc33aa7bfd~mv2.jpg"),
]

ELEC = [
    ("Tharshini Subash", "a3572c_1900bf3f8c9f4275bb3afd38247a5faf~mv2.jpg"),
    ("Zaria Nguyen", "a3572c_86479d3d3c824b06b4519e93c8dc7c29~mv2.jpg"),
    ("Adiba Mahjabeen", "a3572c_696c96bf37a14c569580ac516ff263cc~mv2.png"),
    ("Tanvi Naragoni", "a3572c_fbcbac0559864daa80e49b2258d55056~mv2.jpg"),
    ("Kathy Vo", "a3572c_137f27ba13bd412ca9e7aceddd4c1d3c~mv2.jpg"),
    ("Louisa Marrone", "a3572c_82017196365844cf9b0e246913d08546~mv2.png"),
    ("Adaku Duru", "a3572c_01be6314eeab40f2adc1841cb8c6552c~mv2.jpg"),
    ("Ananda Maharaj", "a3572c_36efe6e6f5a446c0a67e8051cbe39650~mv2.jpg"),
    ("Raquel Susko", "a3572c_14f78adda9014921b631073712537c42~mv2.jpg"),
    ("Aarathi Devakumar", "a3572c_61535b4d24934826af912b8586dc005b~mv2.png"),
    ("Alyssa Bargas", "a3572c_1161338ca8ba49cc9f148da0eaa5b263~mv2.jpg"),
    ("Jennifer Romero", "a3572c_e6c0d1e74a9341cc89fb605327e792ab~mv2.jpg"),
    ("Gael Mamenta", "a3572c_be028e9a341043869b2e4c81bfc81f6a~mv2.jpg"),
    ("Emma Stewart", "a3572c_9f764bc228f344d7b3af0bba0581ca5b~mv2.jpg"),
    ("Azhure Landers", "a3572c_9ce8928832c444e290f05dbb4462f873~mv2.jpg"),
]

PROG = [
    ("Alex Holmes", "a3572c_73bf0d36e8074b639f8a3b7580d4ee5a~mv2.jpg"),
    ("Sanjana Anand", "a3572c_be45fa69107e4c36b91e25ae185f2a2f~mv2.jpg"),
    ("Nisha Murali", "a3572c_b64290cda84d4738ac0e066f99cbf034~mv2.jpg"),
    ("Mackenzie Lloyd", "a3572c_fcaa06c7956b4c02b84f9ebb855ae8b0~mv2.jpg"),
    ("Anna Miley", "a3572c_863483cb3d4841e686c50c2c317d63d6~mv2.jpg"),
    ("Tanvi Kangralkar", "a3572c_82a7132bcea5431baf1f3e1a109a6772~mv2.jpg"),
    ("Parvathi Menon", "a3572c_2fd0f17b1e604826ad2c5df6083418df~mv2.jpg"),
    ("Raquel Susko", "a3572c_83452cf2ccd24073b8ad3f5896d84486~mv2.jpg"),
    ("Alyssa Bargas", "a3572c_e221663c7fa24c689addb7f08d718434~mv2.jpg"),
    ("Adithi Ganesan", "a3572c_d2b00a35f2464c62a912da94fbbc2c00~mv2.jpg"),
]


def officers():
    cards = []
    for name, role, img in OFFICERS:
        cards.append(
            f'<article class="officer"><img src="{IMG}{img}" alt="{name}"><h3>{name}</h3><p>{role}</p></article>'
        )
    return "\n".join(cards)


def people(rows):
    cards = []
    for name, img in rows:
        cards.append(
            f'<article class="person"><img src="{IMG}{img}" alt="{name}"><div class="meta"><h3>{name}</h3></div></article>'
        )
    return "\n".join(cards)


def main():
    body = f'''
    <section class="section">
      <div class="wrap">
        <p class="eyebrow">Leadership</p>
        <h2>2025–2026 officers</h2>
        <p class="intro">The current officer board, carried over from the live Wix site.</p>
        <div class="officer-grid" style="margin-top:28px">{officers()}</div>
      </div>
    </section>
    <section class="section section-dark">
      <div class="wrap">
        <p class="eyebrow">Mechanical</p>
        <h2>Mechanical subteam</h2>
        <div class="team-grid" style="margin-top:28px">{people(MECH)}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <p class="eyebrow">Electrical</p>
        <h2>Electrical subteam</h2>
        <div class="team-grid" style="margin-top:28px">{people(ELEC)}</div>
      </div>
    </section>
    <section class="section section-dark">
      <div class="wrap">
        <p class="eyebrow">Programming</p>
        <h2>Programming subteam</h2>
        <div class="team-grid" style="margin-top:28px">{people(PROG)}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <p class="intro">Want to be on this page next year? <a href="/join/" style="color:var(--maroon);font-weight:600">Join the team</a>. Historical officer photos from earlier seasons remain in the original Wix archive and will be added to an alumni page as we continue the redesign.</p>
      </div>
    </section>
'''
    write(
        "team/index.html",
        "Meet the Team | WIRED AUV",
        "2025–2026 officers and members of WIRED Underwater Robotics.",
        body,
        "/assets/images/team-hero.jpg",
    )


if __name__ == "__main__":
    main()
