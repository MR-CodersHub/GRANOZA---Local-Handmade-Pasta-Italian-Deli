import re

with open('home2.html', 'r', encoding='utf-8') as f:
    h2 = f.read()

print("=== SECTIONS IN home2.html ===")
for m in re.finditer(r'<section[^>]*class="([^"]+)"[^>]*>', h2):
    print("Section:", m.group(1))

print("\n=== CARDS IN home2.html ===")
# Find shape cards
for m in re.finditer(r'<div[^>]*class="([^"]*shape[^"]*)"[^>]*>', h2):
    print("Shape div:", m.group(1))

# Find chef picks
for m in re.finditer(r'<div[^>]*class="([^"]*pick[^"]*|[^"]*chef[^"]*)"[^>]*>', h2):
    print("Chef div:", m.group(1))

# Find salumeria
for m in re.finditer(r'<div[^>]*class="([^"]*salumeria[^"]*|[^"]*deli[^"]*)"[^>]*>', h2):
    print("Salumeria div:", m.group(1))

# Find package / catering
for m in re.finditer(r'<div[^>]*class="([^"]*package[^"]*)"[^>]*>', h2):
    print("Package div:", m.group(1))

# Find testimonial / review
for m in re.finditer(r'<div[^>]*class="([^"]*testimonial[^"]*|[^"]*review[^"]*)"[^>]*>', h2):
    print("Testimonial div:", m.group(1))
