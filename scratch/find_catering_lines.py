with open('catering.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'catering-instructions-section' in line or 'catering-form-section' in line:
        print(f"Line {i+1}: {line.strip()}")
