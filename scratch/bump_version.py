import glob

files = sorted(glob.glob('*.html'))
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('?v=9', '?v=10')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Bumped version to v=10 across all HTML files!")
