with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("=== BLOG.HTML SECTIONS ===")
for m in re.finditer(r'<section[^>]*class="([^"]+)"[^>]*>', text):
    print("Section class:", m.group(1))

# Find buttons in blog cards
for m in re.finditer(r'<(?:button|a)[^>]*class="[^"]*(?:btn|read|cta)[^"]*"[^>]*>([\s\S]*?)</(?:button|a)>', text):
    print("Button:", m.group(0)[:120], "--> Text:", re.sub(r'<[^>]+>', '', m.group(1)).strip())
