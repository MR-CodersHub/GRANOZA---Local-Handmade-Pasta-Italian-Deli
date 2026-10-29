import glob

for fpath in sorted(glob.glob('*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    has_nav_actions = 'class="nav-actions"' in content
    has_mobile_hdr = 'class="mobile-nav-header"' in content
    print(f'{fpath}: nav_actions={has_nav_actions}, mobile_hdr={has_mobile_hdr}')
