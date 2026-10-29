import glob, re

targets = [
    'shape-card',
    'chef-pick-item',
    'deli-pantry-section',
    'catering-split-cards',
    'package-card',
    'reviews-strip',
    'review-mini-card'
]

for fpath in ['css/home2_redesign.css', 'css/style.css']:
    with open(fpath, 'r', encoding='utf-8') as f:
        css = f.read()
    print(f"=== RULES IN {fpath} ===")
    for t in targets:
        matches = re.findall(rf'([^{{}}]*\.{t}[^{{}}]*\s*\{{[^\}}]+\}})', css)
        if matches:
            print(f"Target {t} ({len(matches)} matches):")
            for m in matches[:3]:
                print(m[:250])
                print("---")
