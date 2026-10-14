import re

with open('catering.html', 'r', encoding='utf-8') as f:
    cat = f.read()

print("=== CATERING PACKAGES ===")
m = re.search(r'<div class="package-card[^"]*".*?</div\s*>', cat, re.DOTALL)
if m:
    print(m.group(0)[:500])

print("\n=== DISPLAY BOARDS SECTION ===")
m = re.search(r'Display Boards.*?</section>', cat, re.DOTALL)
if m:
    print(m.group(0)[:800])

print("\n=== EVENTI SU MISURA ===")
m = re.search(r'Eventi su Misura.*?</section>', cat, re.DOTALL)
if m:
    print(m.group(0)[:1200])

with open('blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

print("\n=== BLOG MODAL ===")
m = re.search(r'<div[^>]*class="[^"]*modal[^"]*"[^>]*>.*?</div\s*>', blog, re.DOTALL)
if m:
    print(m.group(0)[:600])

# also search for all modals in all html files
import glob
for fpath in sorted(glob.glob('*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    modals = re.findall(r'<div[^>]*class="[^"]*modal[^"]*"[^>]*>', html)
    if modals:
        print(f"Modals in {fpath}:", modals)
