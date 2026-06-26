"""
update_branding.py
Updates the footer logo in all HTML files to match the header:
  Old: <a href="index.html" class="footer-logo">ALEX<span class="text-gradient">COPY.</span></a>
  New: <a href="index.html" class="footer-logo">
         <img src="img/logo-icon.png" alt="AlexCopy Logo" height="36" class="brand-logo-icon">
         <span class="brand-text-name">ALEX<span class="text-gradient">COPY.</span></span>
       </a>
"""
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))

HTML_FILES = [
    "index.html", "home-2.html", "about.html", "services.html",
    "service-details.html", "pricing.html", "gallery.html",
    "contact.html", "blog.html", "blog-details.html",
    "login.html", "register.html", "coming-soon.html",
    "booking.html", "404.html",
]

# The new footer logo HTML (using relative path img/logo-icon.png)
NEW_FOOTER_LOGO = (
    '<a href="index.html" class="footer-logo">\n'
    '          <img src="img/logo-icon.png" alt="AlexCopy Logo" height="36" class="brand-logo-icon">\n'
    '          <span class="brand-text-name">ALEX<span class="text-gradient">COPY.</span></span>\n'
    '        </a>'
)

# Pattern: match the old footer-logo anchor (text only, no img inside)
FOOTER_PATTERN = re.compile(
    r'<a\s[^>]*class="[^"]*footer-logo[^"]*"[^>]*>ALEX<span[^>]*>COPY\.</span></a>',
    re.DOTALL
)

updated = []
skipped = []

for fname in HTML_FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        skipped.append(fname)
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, count = FOOTER_PATTERN.subn(NEW_FOOTER_LOGO, content)

    if count:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated.append(f"{fname}  ({count} replacement{'s' if count > 1 else ''})")
    else:
        skipped.append(fname)

print("=== Updated files ===")
for x in updated:
    print(" ", x)

print("\n=== Skipped (no match or not found) ===")
for x in skipped:
    print(" ", x)
