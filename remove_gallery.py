import os
import glob
import re

html_files = glob.glob('c:/Users/Shalani A/Documents/Shalan/Client Projects(JUNE)/Freelance Copywriter (Direct Response & Sales Pages)/Freelance_Copywriter_Direct_Response_Sales_Pages/*.html')

pattern = re.compile(r'\s*<li class="nav-item"><a class="nav-link(?: active)?" href="gallery\.html">Gallery</a></li>\s*\n?', re.IGNORECASE)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('\n', content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No match found in {file_path}")

print("Done.")
