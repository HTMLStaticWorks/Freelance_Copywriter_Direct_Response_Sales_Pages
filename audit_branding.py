import re, os

BASE = r"c:\Users\Shalani A\Documents\Shalan\Client Projects(JUNE)\Freelance Copywriter (Direct Response & Sales Pages)\Freelance_Copywriter_Direct_Response_Sales_Pages"
HTML_FILES = [
    "index.html","home-2.html","about.html","services.html","service-details.html",
    "pricing.html","gallery.html","contact.html","blog.html","blog-details.html",
    "login.html","register.html","coming-soon.html","booking.html","404.html"
]

print("=== BRANDING AUDIT ===\n")
all_ok = True
for f in HTML_FILES:
    p = os.path.join(BASE, f)
    content = open(p, encoding="utf-8").read()
    has_header_icon = bool(re.search(r'class="navbar-brand.{0,200}logo-icon\.png', content, re.DOTALL))
    has_header_name = bool(re.search(r'brand-text-name', content))
    has_footer_icon = bool(re.search(r'class="footer-logo".{0,300}logo-icon\.png', content, re.DOTALL))
    has_old_footer  = bool(re.search(r'class="footer-logo"[^>]*>ALEX', content))
    has_favicon     = bool(re.search(r"favicon\.ico", content))
    status = "OK" if not has_old_footer else "NEEDS FIX"
    if has_old_footer:
        all_ok = False
    print(f"{f} [{status}]:")
    print(f"  Header icon+name : {has_header_icon and has_header_name}")
    print(f"  Footer icon+name : {has_footer_icon}  |  Old text-only footer: {has_old_footer}")
    print(f"  Favicon tags     : {has_favicon}")
    print()

print("ALL OK" if all_ok else "SOME ISSUES FOUND")
