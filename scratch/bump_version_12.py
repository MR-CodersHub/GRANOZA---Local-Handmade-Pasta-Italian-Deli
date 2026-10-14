import glob

files = sorted(glob.glob('*.html'))
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('?v=11', '?v=12')
    c = c.replace('?v=10', '?v=12')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Bumped version to v=12 across all HTML files!")
