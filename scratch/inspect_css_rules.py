import re

with open('css/redesign_sections.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = [
    'hero-cta-ghost',
    'shs-seal',
    'shs-step',
    'pfh-spec',
    'pfh-desc',
    'dps-cc',
    'dps-flavor-tag',
    'dps-seal',
    'cgs-ratio',
    'crs-metric',
    'crs-label',
    'cfs-secret',
    'cgs-recipe'
]

for c in classes:
    matches = re.findall(rf'(\.[a-zA-Z0-9_\-]*{c}[a-zA-Z0-9_\-]*\s*\{{[^\}}]+\}})', css)
    print(f"=== Class match for {c} ({len(matches)} rules) ===")
    for m in matches[:3]:
        print(m[:250])
    print()
