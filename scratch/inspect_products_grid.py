with open('products.html', 'r', encoding='utf-8') as f:
    p = f.read()

import re
m = re.search(r'<div class="product-grid-6">', p)
if m:
    print("=== PRODUCT-GRID-6 SNIPPET ===")
    print(p[m.start():m.start()+1500])
