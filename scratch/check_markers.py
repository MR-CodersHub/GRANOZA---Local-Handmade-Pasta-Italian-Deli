# -*- coding: utf-8 -*-
"""
Script to update index.html with 100% unique, non-repetitive section layouts,
properly formatted prices ($14.50, $15.00, etc.), and clean typography without encoding artifacts.
"""
import sys

index_html_path = r"c:\Users\dines\OneDrive\Desktop\italian\index.html"

with open(index_html_path, "r", encoding="utf-8") as f:
    orig_content = f.read()

# Verify header and footer boundaries
header_marker = '<!-- =========================================================================\n       SECTION 1: HERO'
footer_marker = '  <!-- =========================================================================\n       MAIN FOOTER'

if header_marker not in orig_content or footer_marker not in orig_content:
    # Alternative boundary search
    idx_hero = orig_content.find('id="hero-section"')
    idx_footer = orig_content.find('<footer class="main-footer"')
    print(f"Indices: hero={idx_hero}, footer={idx_footer}")
else:
    print("Found standard markers!")
