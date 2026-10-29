import glob
import re

for html in glob.glob('*.html'):
    with open(html, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'src="js/main\.js(\?v=\d+)?"', 'src="js/main.js?v=6"', c)
    with open(html, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated {html}')
