import glob

files = sorted(glob.glob('*.html'))
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'theme_rtl.css' not in content:
        # replace </head> or right after style.css
        target = '<link rel="stylesheet" href="css/style.css'
        idx = content.find(target)
        if idx != -1:
            end_line_idx = content.find('\n', idx)
            insert_str = '\n  <link rel="stylesheet" href="css/theme_rtl.css?v=9">'
            content = content[:end_line_idx] + insert_str + content[end_line_idx:]
            print(f'{fpath}: linked theme_rtl.css')
        else:
            print(f'{fpath}: target not found!')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done linking theme_rtl.css across all files!")
