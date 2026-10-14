import glob, re

HEAD_SCRIPT = '''  <!-- Immediate Theme & RTL Init Script (prevents flash) -->
  <script>
    (function() {
      try {
        var theme = localStorage.getItem('granoza_theme');
        if (theme === 'dark' || (!theme && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
          document.documentElement.setAttribute('data-theme', 'dark');
        } else {
          document.documentElement.setAttribute('data-theme', 'light');
        }
        var dir = localStorage.getItem('granoza_direction');
        if (dir === 'rtl') {
          document.documentElement.setAttribute('dir', 'rtl');
        } else {
          document.documentElement.setAttribute('dir', 'ltr');
        }
      } catch (e) {}
    })();
  </script>
'''

TOGGLES_HTML = '''        <button type="button" class="theme-toggle-btn" id="themeToggleBtn" aria-label="Toggle Dark / Light Theme" title="Toggle Theme">
          <i class="fa-solid fa-moon"></i>
        </button>
        <button type="button" class="rtl-toggle-btn" id="rtlToggleBtn" aria-label="Toggle RTL / LTR Layout" title="Toggle RTL / LTR">
          <i class="fa-solid fa-right-left"></i>
          <span class="rtl-text">RTL</span>
        </button>
'''

MOBILE_CONTROLS_HTML = '''      <div class="mobile-nav-controls">
        <button type="button" class="theme-toggle-btn mobile-theme-btn" aria-label="Toggle Dark / Light Theme" title="Toggle Theme">
          <i class="fa-solid fa-moon"></i>
        </button>
        <button type="button" class="rtl-toggle-btn mobile-rtl-btn" aria-label="Toggle RTL / LTR Layout" title="Toggle RTL / LTR">
          <i class="fa-solid fa-right-left"></i>
          <span class="rtl-text">RTL</span>
        </button>
      </div>
'''

files = sorted(glob.glob('*.html'))
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert Head script if not present
    if 'granoza_theme' not in content:
        # insert right before </head>
        content = content.replace('</head>', HEAD_SCRIPT + '</head>')
        print(f'{fpath}: inserted head script')

    # 2. Insert Desktop Toggles in .nav-actions
    if 'id="themeToggleBtn"' not in content:
        # replace right before <button type="button" class="cart-toggle-btn"
        pattern = r'(\s*<div class="nav-actions">\s*)(\s*<button type="button" class="cart-toggle-btn")'
        def repl_nav(m):
            return m.group(1) + TOGGLES_HTML + m.group(2)
        content, count = re.subn(pattern, repl_nav, content, count=1)
        print(f'{fpath}: nav-actions updated (count={count})')

    # 3. Insert Mobile Controls in .mobile-nav-header
    if 'mobile-theme-btn' not in content:
        # replace before <button type="button" class="mobile-nav-close"
        pattern = r'(\s*<button type="button" class="mobile-nav-close"[^>]*>)'
        def repl_mob(m):
            return '\n' + MOBILE_CONTROLS_HTML + m.group(1)
        content, count = re.subn(pattern, repl_mob, content, count=1)
        print(f'{fpath}: mobile-nav-header updated (count={count})')

    # 4. Bump version to v=9
    content = content.replace('style.css?v=8', 'style.css?v=9')
    content = content.replace('redesign_sections.css?v=8', 'redesign_sections.css?v=9')
    content = content.replace('home2_redesign.css?v=8', 'home2_redesign.css?v=9')
    content = content.replace('about_redesign.css?v=8', 'about_redesign.css?v=9')
    content = content.replace('main.js?v=8', 'main.js?v=9')
    content = content.replace('main.js', 'main.js?v=9')
    content = content.replace('main.js?v=9?v=9', 'main.js?v=9')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML files processed successfully!")
