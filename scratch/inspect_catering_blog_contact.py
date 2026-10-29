import re

with open('catering.html', 'r', encoding='utf-8') as f:
    catering = f.read()

print("=== CATERING.HTML ===")
for m in re.finditer(r'<section[^>]*class="([^"]+)"[^>]*>', catering):
    print("Section class:", m.group(1))

# Search for date input
for m in re.finditer(r'<input[^>]*type="date"[^>]*>', catering):
    print("Date input:", m.group(0))

# Search for Italian titles or instructions
for m in re.finditer(r'<h[1-4][^>]*>([\s\S]*?)</h[1-4]>', catering):
    text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print("Heading:", text)

for m in re.finditer(r'class="[^"]*eyebrow[^"]*"[^>]*>([\s\S]*?)<', catering):
    print("Eyebrow:", m.group(1).strip())
