import os
import re

html_files = [
    'index.html',
    'home2.html',
    'about.html',
    'products.html',
    'catering.html',
    'blog.html',
    'contact.html'
]

cart_nav_link_snippet = '''      <a href="#" class="mobile-nav-link mobile-cart-trigger" aria-label="Open Shopping Cart">
        <span class="mobile-cart-label-wrap">
          <i class="fa-solid fa-basket-shopping" style="color:var(--golden-yellow); margin-right:8px; font-size:1.05rem;"></i>
          <span>Order Basket / Cart</span>
        </span>
        <span class="mobile-cart-badge-pill">
          <strong class="cart-badge-count">0</strong> items
          <i class="fa-solid fa-angle-right" style="margin-left:6px; font-size:0.75rem; opacity:0.75;"></i>
        </span>
      </a>'''

mobile_cart_btn_snippet = '''        <button type="button" class="cart-toggle-btn mobile-cart-btn" aria-label="Open Cart Order Drawer" title="Open Cart Basket">
          <i class="fa-solid fa-basket-shopping"></i>
          <span class="cart-badge">0</span>
        </button>'''

for fname in html_files:
    if not os.path.exists(fname):
        print(f"File not found: {fname}")
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # 1. Update header cart-toggle-btn to have d-none-mobile if not already present
    # Matches <button type="button" class="cart-toggle-btn"
    content = re.sub(
        r'<button\s+type="button"\s+class="cart-toggle-btn"(?!\s+d-none-mobile)',
        '<button type="button" class="cart-toggle-btn d-none-mobile"',
        content
    )

    # 2. Add mobile-cart-btn into .mobile-nav-controls if not present
    if 'mobile-cart-btn' not in content:
        # Match closing of mobile-nav-controls
        pattern = r'(<div class="mobile-nav-controls">[\s\S]*?)(</div>)'
        def add_cart_btn(match):
            controls_inner = match.group(1)
            end_div = match.group(2)
            return controls_inner + '\n' + mobile_cart_btn_snippet + '\n      ' + end_div
        content = re.sub(pattern, add_cart_btn, content, count=1)

    # 3. Add mobile-cart-trigger into .mobile-nav-links if not present
    if 'mobile-cart-trigger' not in content:
        # Match closing of mobile-nav-links
        pattern = r'(<div class="mobile-nav-links">[\s\S]*?)(</div>)'
        def add_cart_link(match):
            links_inner = match.group(1)
            end_div = match.group(2)
            return links_inner + '\n' + cart_nav_link_snippet + '\n    ' + end_div
        content = re.sub(pattern, add_cart_link, content, count=1)

    # 4. Bump cache buster from ?v=15 to ?v=16 (or ?v=\d+)
    content = re.sub(r'\?v=\d+', '?v=16', content)

    if content != orig_content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname} successfully.")
    else:
        print(f"No changes needed for {fname}.")

print("Completed processing all HTML files.")
