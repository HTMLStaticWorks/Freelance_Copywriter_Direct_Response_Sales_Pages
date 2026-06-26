import os
import glob
import re

html_files = glob.glob('c:/Users/Shalani A/Documents/Shalan/Client Projects(JUNE)/Freelance Copywriter (Direct Response & Sales Pages)/Freelance_Copywriter_Direct_Response_Sales_Pages/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('href="booking.html"', 'href="contact.html"')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No match found in {file_path}")

print("Done.")
