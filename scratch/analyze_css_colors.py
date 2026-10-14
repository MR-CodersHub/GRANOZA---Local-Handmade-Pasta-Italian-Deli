import re

with open('css/redesign_sections.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find all color and background declarations
rules = re.findall(r'([^{}]+)\s*\{\s*([^}]+)\}', css)

print(f"Total rules in redesign_sections.css: {len(rules)}")
for selector, body in rules:
    selector = selector.strip()
    if any(k in body for k in ['color:', 'background:', 'background-color:']):
        # check if it uses navy-deep or text-dark or pure-white or beige or ivory
        if any(c in body for c in ['var(--navy-deep)', 'var(--text-dark)', 'var(--text-muted)', 'var(--warm-ivory)', 'var(--pure-white)', '#fff', '#ffffff', '#061A46', '#1b2330']):
            for line in body.split(';'):
                line = line.strip()
                if any(c in line for c in ['color', 'background']):
                    # print selector and line
                    print(f"{selector[:40]} -> {line}")
