with open('blog.html', 'r', encoding='utf-8') as f:
    blog = f.read()

import re

# find any modal in blog.html
for m in re.finditer(r'<div[^>]*modal[^>]*>.*?</div\s*>', blog, re.DOTALL):
    print("Modal in blog.html:", m.group(0)[:500])

# find modal in js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

for m in re.finditer(r'function\s+open[A-Za-z0-9_]*Modal[^{]*\{[^}]+\}', js):
    print("Modal function in js/main.js:", m.group(0)[:300])

for m in re.finditer(r'modal[A-Za-z0-9_\-]*\s*\{[^}]+\}', js):
    print("Modal CSS/JS:", m.group(0)[:200])

# Also check modal CSS in css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

for m in re.finditer(r'\.modal[A-Za-z0-9_\-]*\s*\{[^}]+\}', css):
    print("Modal CSS in style.css:", m.group(0)[:200])
