import glob, re

for fpath in sorted(glob.glob('*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    sections = re.findall(r'<section[^>]*class="([^"]+)"[^>]*>', html)
    print(f"=== {fpath} ({len(sections)} sections) ===")
    for s in sections:
        print("  - section:", s)

    # find any elements with style="background... or class="bg-..."
    inline_bgs = re.findall(r'<[^>]+(?:style="[^"]*background[^"]*"|class="[^"]*bg-[^"]*")[^>]*>', html)
    if inline_bgs:
        print(f"  Inline/bg-classes ({len(inline_bgs)}):")
        for b in inline_bgs[:5]:
            print("   ", b[:100])
    print()
