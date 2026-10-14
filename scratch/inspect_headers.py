import glob, re

for fpath in sorted(glob.glob('*.html')):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    m_nav = re.search(r'<div class="nav-actions">.*?</div>', content, re.DOTALL)
    m_mob = re.search(r'<div class="mobile-nav-header">.*?</div>', content, re.DOTALL)
    print('===', fpath, '===')
    if m_nav:
        print('NAV ACTIONS:\n', m_nav.group(0))
    if m_mob:
        print('MOBILE HDR:\n', m_mob.group(0))
