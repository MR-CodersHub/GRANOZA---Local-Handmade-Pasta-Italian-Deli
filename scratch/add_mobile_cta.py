import glob

html_files = sorted(glob.glob('*.html'))
cta_html = '''    <div class="mobile-drawer-cta-wrap">
      <a href="catering.html" class="btn btn-gold mobile-menu-cta-btn">
        <i class="fa-solid fa-bell-concierge"></i> Catering Quote
      </a>
    </div>'''

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'mobile-drawer-cta-wrap' not in content:
        idx = content.find('class="mobile-nav-footer"')
        if idx != -1:
            div_idx = content.rfind('</div>', 0, idx)
            if div_idx != -1:
                new_content = content[:div_idx+6] + '\n' + cta_html + content[div_idx+6:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Added mobile CTA button to {fpath}')
            else:
                print(f'Could not find closing div in {fpath}')
        else:
            print(f'mobile-nav-footer not found in {fpath}')
    else:
        print(f'Already has mobile CTA in {fpath}')
