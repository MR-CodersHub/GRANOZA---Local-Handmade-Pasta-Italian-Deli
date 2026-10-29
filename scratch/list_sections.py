import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all section tags
sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*>', content)
print("Sections in index.html:")
for s in sections:
    print(f" - {s}")
