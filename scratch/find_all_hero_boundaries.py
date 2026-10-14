import os

WORKSPACE = r"c:\Users\dines\OneDrive\Desktop\italian"
files = ["home2.html", "about.html", "products.html", "catering.html", "blog.html", "contact.html"]

for f in files:
    path = os.path.join(WORKSPACE, f)
    with open(path, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    # Find hero section start and end
    if "hero-home-2" in c:
        start_tag = 'class="hero-home-2"'
    elif "catering-hero-section" in c:
        start_tag = 'class="catering-hero-section"'
    elif "page-hero" in c:
        start_tag = 'class="page-hero"'
    else:
        start_tag = "UNKNOWN"
    
    idx = c.find(start_tag)
    comment_idx = c.rfind("<!--", 0, idx)
    end_sec_idx = c.find("</section>", idx) + len("</section>")
    
    print(f"{f}: start_tag={start_tag}, comment_idx={comment_idx}, end_sec_idx={end_sec_idx}")
    print(f"  Snippet at start: {repr(c[comment_idx:comment_idx+60])}")
    print(f"  Snippet at end: {repr(c[end_sec_idx:end_sec_idx+60])}")
