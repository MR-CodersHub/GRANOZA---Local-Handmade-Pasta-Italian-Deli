with open('home2.html', 'r', encoding='utf-8') as f:
    h2 = f.read()

import re

# Snippet of shape-card
m = re.search(r'<div class="shape-card">.*?</div\s*>', h2, re.DOTALL)
if m:
    print("=== SHAPE CARD HTML ===")
    print(m.group(0)[:500])

# Snippet of chef-pick-item
m = re.search(r'<div class="chef-pick-item">.*?</div\s*>', h2, re.DOTALL)
if m:
    print("=== CHEF PICK ITEM HTML ===")
    print(m.group(0)[:500])

# Snippet of deli-pantry-section
m = re.search(r'<section class="deli-pantry-section"[^>]*>.*?</section\s*>', h2, re.DOTALL)
if m:
    print("=== DELI PANTRY SECTION HTML ===")
    print(m.group(0)[:600])

# Snippet of home2-catering-section
m = re.search(r'<section class="home2-catering-section"[^>]*>.*?</section\s*>', h2, re.DOTALL)
if m:
    print("=== HOME2 CATERING SECTION HTML ===")
    print(m.group(0)[:600])

# Snippet of home2-reviews-section
m = re.search(r'<section class="home2-reviews-section"[^>]*>.*?</section\s*>', h2, re.DOTALL)
if m:
    print("=== HOME2 REVIEWS SECTION HTML ===")
    print(m.group(0)[:600])
