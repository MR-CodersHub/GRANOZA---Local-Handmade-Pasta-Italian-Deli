import glob
import os
import re

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    size = os.path.getsize(f)
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    has_doctype = '<!DOCTYPE html>' in c
    has_head = '<head>' in c and '</head>' in c
    has_body = '<body' in c and '</body>' in c
    has_title = '<title>' in c and '</title>' in c
    
    # check images
    imgs = re.findall(r'src=["\'](images/[^"\']+)["\']', c)
    missing_imgs = [img for img in imgs if not os.path.exists(img)]
    
    # check css
    csss = re.findall(r'href=["\'](css/[^"\']+)["\']', c)
    missing_css = [css.split('?')[0] for css in csss if not os.path.exists(css.split('?')[0])]
    
    # check js
    jss = re.findall(r'src=["\'](js/[^"\']+)["\']', c)
    missing_js = [js.split('?')[0] for js in jss if not os.path.exists(js.split('?')[0])]
    
    print(f"{f}: {size} bytes | Doctype: {has_doctype} | Head: {has_head} | Body: {has_body} | Title: {has_title} | Missing imgs: {len(missing_imgs)} | Missing css: {len(missing_css)} | Missing js: {len(missing_js)}")
    if missing_imgs:
        print(f"  Missing imgs: {missing_imgs}")
    if missing_css:
        print(f"  Missing css: {missing_css}")
    if missing_js:
        print(f"  Missing js: {missing_js}")
