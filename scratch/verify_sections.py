import re

with open('about.html', 'r', encoding='utf-8') as f:
    abt = f.read()

sections = re.findall(r'<section class="([^"]+)"', abt)
print('about.html sections:')
for s in sections:
    print(' -', s)

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx_sections = re.findall(r'<section class="([^"]+)"', idx)
print('\nindex.html sections:')
for s in idx_sections:
    print(' -', s)
