import re

def search_css(fpath, terms):
    with open(fpath, 'r', encoding='utf-8') as f:
        css = f.read()
    print(f"=== SEARCH IN {fpath} ===")
    for term in terms:
        matches = re.findall(rf'([^{{}}]*\.{term}[^{{}}]*\s*\{{[^\}}]+\}})', css)
        print(f"Term: {term} ({len(matches)} matches)")
        for m in matches[:3]:
            print("  ", m[:200])

search_css('css/style.css', ['product-card', 'about-stat', 'pmb-seal', 'pmb-check', 'hst-tag'])
search_css('css/about_redesign.css', ['about-stat', 'hst-tag', 'pmb-seal', 'pmb-check', 'pmb-quote', 'pmb-tile'])
