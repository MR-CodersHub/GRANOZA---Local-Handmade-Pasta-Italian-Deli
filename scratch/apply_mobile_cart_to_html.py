import glob
import re

html_files = sorted(glob.glob('*.html'))

mobile_cart_trigger_html = '''      <a href="#" class="mobile-nav-link mobile-cart-trigger" aria-label="Open Shopping Cart">
        <span class="mobile-cart-label-wrap">
          <i class="fa-solid fa-basket-shopping" style="color:var(--golden-yellow); margin-right:8px; font-size:1.1rem;"></i>
          <span>Order Basket / Cart</span>
        </span>
        <span class="mobile-cart-badge-pill">
          <strong class="cart-badge-count">0</strong> items
          <i class="fa-solid fa-angle-right" style="margin-left:6px; font-size:0.75rem; opacity:0.75;"></i>
        </span>
      </a>'''

mobile_cart_btn_in_controls = '''        <button type="button" class="cart-toggle-btn mobile-cart-btn mobile-cart-trigger" aria-label="Open Shopping Cart" title="Open Basket">
          <i class="fa-solid fa-basket-shopping"></i>
          <span class="cart-badge cart-badge-count">0</span>
        </button>'''

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Ensure header cart-toggle-btn has d-none-mobile
    # Target <button type="button" class="cart-toggle-btn"
    content = re.sub(
        r'<button\s+type="button"\s+class="cart-toggle-btn"(?!\s+d-none-mobile)',
        '<button type="button" class="cart-toggle-btn d-none-mobile"',
        content
    )

    # 2. Add mobile-cart-trigger to .mobile-nav-links if not present
    if 'mobile-cart-trigger' not in content:
        # Insert right after <div class="mobile-nav-links">
        pattern = r'(<div class="mobile-nav-links">)'
        content = re.sub(pattern, r'\1\n' + mobile_cart_trigger_html, content, count=1)

    # 3. Add mobile-cart-btn to .mobile-nav-controls if not present
    if 'mobile-cart-btn' not in content:
        pattern = r'(<div class="mobile-nav-controls">[\s\S]*?)(</div>)'
        def add_btn(m):
            return m.group(1) + '\n' + mobile_cart_btn_in_controls + '\n      ' + m.group(2)
        content = re.sub(pattern, add_btn, content, count=1)

    # 4. Bump cache busters to v=17
    content = re.sub(r'(\.css|\.js)\?v=\d+', r'\1?v=17', content)

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")
    else:
        print(f"No changes needed for {fpath}")

print("HTML update script finished.")
