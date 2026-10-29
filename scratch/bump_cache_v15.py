import glob

html_files = sorted(glob.glob('*.html'))
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('style.css?v=14', 'style.css?v=15')
    content = content.replace('style.css?v=13', 'style.css?v=15')
    content = content.replace('theme_rtl.css?v=14', 'theme_rtl.css?v=15')
    content = content.replace('theme_rtl.css?v=13', 'theme_rtl.css?v=15')
    content = content.replace('redesign_sections.css?v=12', 'redesign_sections.css?v=15')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Bumped cache to v=15 in {fpath}')
