with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

hero_idx = c.find('class="hero-home-1"')
# backtrack to the comment before hero
comment_idx = c.rfind('<!--', 0, hero_idx)

footer_idx = c.find('<footer class="main-footer"')
footer_comment_idx = c.rfind('<!--', 0, footer_idx)

print('Comment idx:', comment_idx)
print('Snippet before hero:\n', c[comment_idx:comment_idx+120])
print('Footer comment idx:', footer_comment_idx)
print('Snippet at footer:\n', c[footer_comment_idx:footer_comment_idx+120])
