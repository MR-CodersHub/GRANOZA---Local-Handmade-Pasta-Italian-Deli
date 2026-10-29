import urllib.request
import re
import os

pages = ['index.html', 'home2.html', 'about.html', 'products.html', 'catering.html', 'blog.html', 'contact.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    has_cinematic = 'hero-cinematic-inner' in html
    has_card = 'hero-card-showcase' in html
    has_stat = 'hero-stat-tower' in html
    has_artifact = 'â' in html
    
    # Check images inside hero
    start = html.find('hero-bg-layers')
    end = html.find('</section>', start)
    hero_chunk = html[start:end]
    imgs = re.findall(r'src="([^"]+)"', hero_chunk)
    
    # Verify all imgs exist on disk
    all_imgs_exist = all(os.path.exists(img) for img in imgs)
    
    req = urllib.request.urlopen(f'http://localhost:8090/{p}')
    print(f"{p}: status={req.status}, size={len(html)}, cinematic={has_cinematic}, card={has_card}, stat={has_stat}, artifact={has_artifact}, all_imgs_exist={all_imgs_exist}")
    print(f"   images: {imgs}")
