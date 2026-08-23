const NAV = [
  { href: "/", label: "Home" },
  { href: "/vehicles/", label: "Vehicles" },
  { href: "/team/", label: "Team" },
  { href: "/gallery/", label: "Gallery" },
  { href: "/achievements/", label: "Achievements" },
  { href: "/join/", label: "Join" },
  { href: "/faq/", label: "FAQ" },
  { href: "/sponsors/", label: "Sponsors" },
  { href: "/contact/", label: "Contact" },
];

function currentPath() {
  const path = window.location.pathname.replace(/index\.html$/, "");
  return path.endsWith("/") || path === "" ? path || "/" : `${path}/`;
}

function isCurrent(href) {
  const path = currentPath();
  if (href === "/") return path === "/";
  return path.startsWith(href);
}

function headerHtml() {
  const links = NAV.map((item) => {
    const current = isCurrent(item.href) ? ' aria-current="page"' : "";
    return `<a href="${item.href}"${current}>${item.label}</a>`;
  }).join("");

  return `
    <a class="skip" href="#content">Skip to content</a>
    <header class="site-header">
      <div class="wrap">
        <a class="brand" href="/">
          <svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true">
            <rect width="48" height="48" rx="12" fill="#500000"/>
            <path d="M8 30c6-10 10-10 16 0s10 10 16 0" fill="none" stroke="#3AD4C4" stroke-width="2.4"/>
            <ellipse cx="24" cy="22" rx="11" ry="5.5" fill="none" stroke="#C9A227" stroke-width="2"/>
            <circle cx="33" cy="22" r="2.2" fill="#C9A227"/>
          </svg>
          <span class="brand-text">
            <strong>WIRED</strong>
            <span>Underwater Robotics</span>
          </span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">☰</button>
        <nav class="nav" id="site-nav">${links}</nav>
      </div>
    </header>
  `;
}

function footerHtml() {
  return `
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
      <div class="wrap legal">© ${new Date().getFullYear()} TAMU WIRED Underwater Robotics. Formerly REAF / WE REAF.</div>
    </footer>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  const headerMount = document.getElementById("site-header");
  const footerMount = document.getElementById("site-footer");
  if (headerMount) headerMount.outerHTML = headerHtml();
  if (footerMount) footerMount.outerHTML = footerHtml();

  document.querySelectorAll("#site-nav a").forEach((link) => {
    const href = link.getAttribute("href");
    if (href && isCurrent(href)) link.setAttribute("aria-current", "page");
  });

  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const data = new FormData(form);
      const name = String(data.get("name") || "");
      const email = String(data.get("email") || "");
      const message = String(data.get("message") || "");
      const subject = encodeURIComponent(`WIRED AUV inquiry from ${name}`);
      const body = encodeURIComponent(`${message}\n\n— ${name}\n${email}`);
      window.location.href = `mailto:reaf.tamu@gmail.com?subject=${subject}&body=${body}`;
    });
  }
});
