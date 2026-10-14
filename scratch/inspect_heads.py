import glob, re

for fpath in sorted(glob.glob('*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    m_head = re.search(r'<head>.*?</head>', content, re.DOTALL)
    print('===', fpath, '===')
    if m_head:
        lines = m_head.group(0).split('\n')
        print('\n'.join(lines[:15]))
