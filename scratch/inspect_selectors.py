import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def show_context(pattern, name, length=300):
    m = re.search(pattern, html)
    if m:
        start = max(0, m.start() - 100)
        end = min(len(html), m.end() + length)
        print(f"=== {name} ===")
        print(html[start:end])
        print("================\n")
    else:
        print(f"NOT FOUND: {name}")

show_context(r'Shop Fresh Pasta', 'Hero Buttons')
show_context(r'26 Years', '26 Years Badge')
show_context(r'Vintage Treviso', 'Story Timeline')
show_context(r'Altamura Semolina', 'Pappardelle Specs')
show_context(r'Campania', 'Sourcing Cards')
show_context(r'The Sacred Pasta Ratio', 'Sacred Ratio')
show_context(r'The Starch Water Secret', 'Starch Water Secret')
