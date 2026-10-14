import re

with open('products.html', 'r', encoding='utf-8') as f:
    p = f.read()

m = re.search(r'<div class="([^"]*product[^"]*)"[^>]*>', p)
if m:
    print("First product div:", m.group(0))

matches = re.findall(r'<div class="([^"]*card[^"]*|[^"]*product[^"]*)"', p)
print("Unique product/card classes:", sorted(list(set(matches))))

m = re.search(r'<div class="product-item-card".*?</div\s*>', p, re.DOTALL)
if m:
    print("=== PRODUCT ITEM CARD HTML ===")
    print(m.group(0)[:600])

# check linked stylesheets in products.html
m_head = re.search(r'<head>.*?</head>', p, re.DOTALL)
if m_head:
    print("=== HEAD IN products.html ===")
    for line in m_head.group(0).split('\n'):
        if 'css' in line or 'link' in line:
            print(" ", line.strip())
