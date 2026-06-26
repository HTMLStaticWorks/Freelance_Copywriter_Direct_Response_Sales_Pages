import os
import re

html_files = [
    "index.html", "home-2.html", "about.html", "services.html",
    "service-details.html", "pricing.html", "gallery.html",
    "contact.html", "blog.html", "blog-details.html",
    "login.html", "register.html", "coming-soon.html",
    "booking.html", "404.html"
]

favicon_tags = """  <link rel="icon" href="img/favicon.ico" sizes="any">
  <link rel="icon" href="img/favicon-32x32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="img/favicon-16x16.png" type="image/png" sizes="16x16">
  <link rel="apple-touch-icon" href="img/apple-touch-icon.png">"""

brand_tag = """<a class="navbar-brand d-flex align-items-center gap-2" href="index.html">
          <img src="img/logo-icon.png" alt="Brand Logo" height="36" class="brand-logo-icon"> 
          <span class="brand-text-name fw-bold">ALEX<span class="text-gradient">COPY.</span></span>
        </a>"""

for file in html_files:
    if not os.path.exists(file):
        print(f"File {file} not found")
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace favicons
    # Look for <link rel="icon" ...> or similar
    content = re.sub(r'<link rel="icon"[^>]*>', favicon_tags, content, count=1)
    
    # Also if there are multiple or if there are shortcut icons, we can remove them.
    # Actually, replacing the first one and removing the others is safer, 
    # but since there's only 1 favicon tag usually in this template:
    # <link rel="icon" href="img/favicon.png" type="image/png">
    
    # Replace navbar-brand
    # We match <a ... class="navbar-brand ...>...</a>
    # Note: re.sub with re.DOTALL to match across lines
    content = re.sub(r'<a[^>]*class="[^"]*navbar-brand[^"]*"[^>]*>.*?</a>', brand_tag, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file}")

