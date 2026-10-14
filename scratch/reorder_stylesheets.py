import glob, re

files = sorted(glob.glob('*.html'))
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing theme_rtl.css link line
    content = re.sub(r'\s*<link rel="stylesheet" href="css/theme_rtl\.css\?v=9">\s*', '\n', content)

    # Insert right before <!-- Immediate Theme & RTL Init Script
    if '<!-- Immediate Theme & RTL Init Script' in content:
        content = content.replace('<!-- Immediate Theme & RTL Init Script', '<!-- Theme & RTL Stylesheet -->\n  <link rel="stylesheet" href="css/theme_rtl.css?v=9">\n\n  <!-- Immediate Theme & RTL Init Script')
    elif '</head>' in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="css/theme_rtl.css?v=9">\n</head>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Stylesheet order updated so theme_rtl.css is always loaded last!")
