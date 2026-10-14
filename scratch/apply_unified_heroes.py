# -*- coding: utf-8 -*-
"""
Redesign Hero sections for home2.html, about.html, products.html, catering.html, blog.html, and contact.html.
All pages are updated to have the EXACT SAME HEIGHT (500px min/max-height: 480px-560px),
using the exact cinematic 2-column split engine of index.html.
"""
import os
import re

WORKSPACE = r"c:\Users\dines\OneDrive\Desktop\italian"
STYLE_CSS = os.path.join(WORKSPACE, "css", "style.css")

HERO_HTML_MAP = {
    "home2.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="hero-home-2" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/hero_home2.jpg" class="hero-bg-img" alt="Granoza Live Bottega Extrusions"
        onerror="this.src='images/hero_bowl.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Edizione Speciale &bull; Bologna Live Atelier</span>
        </div>
        <h1>Today's Artisan Harvest, <br><em class="hero-italic-accent">Rolled Fresh</em> Before Sunrise.</h1>
        <p class="hero-desc">Daily dough hydrations, active bronze dies, and seasonal cellar arrivals from Bologna and Bari &mdash; tracked live from our wooden tables.</p>
        <div class="hero-cta-row">
          <a href="products.html" class="hero-cta-primary">
            <span>Order Fresh Batch</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <a href="#chef-recommendations" class="hero-cta-ghost">Chef's Picks</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-circle-nodes"></i> 3 Active Extrusions</div>
          <div class="htr-item"><i class="fa-solid fa-temperature-arrow-down"></i> Slow Air-Drying</div>
          <div class="htr-item"><i class="fa-solid fa-door-open"></i> Deli Counter Open</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/chef_rolling.jpg" alt="Master pastaio rolling golden egg sfoglia"
              onerror="this.src='images/kitchen.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-wheat-awn"></i>
              <span>Live Extrusions<br><small>Batch #104 Active</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-circle" style="color:#10b981; font-size:0.5rem;"></i>
              <span>Rolling Now &bull; Tagliatelle all'Uovo</span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">8<small>kg</small></span>
              <span class="hsb-label">Batch Left</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">10<small>yolks</small></span>
              <span class="hsb-label">Per Kilo Flour</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">3<small>min</small></span>
              <span class="hsb-label">Cook Time</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

    "about.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="page-hero" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/hero_about.jpg" class="hero-bg-img" alt="Italian culinary heritage and wooden table"
        onerror="this.src='images/italian_dining.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <span>About Our Heritage</span>
        </nav>
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Tradizione &bull; Since 1998 &bull; Bologna</span>
        </div>
        <h1>Artisans of the <br><em class="hero-italic-accent">Wooden Table</em> &amp; Sfoglia</h1>
        <p class="hero-desc">Founded on timeless Emilian principles, Granoza preserves the ancient dignity of hand-rolled sfoglia, slow bronze extrusion, and genuine neighborhood Italian deli culture.</p>
        <div class="hero-cta-row">
          <a href="#about-philosophy" class="hero-cta-primary">
            <span>Our Heritage Story</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <a href="#about-methods" class="hero-cta-ghost">Ancestral Methods</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-wheat-awn"></i> 100% Altamura Wheat</div>
          <div class="htr-item"><i class="fa-solid fa-shield-halved"></i> Zero Chemical Additives</div>
          <div class="htr-item"><i class="fa-solid fa-clock-rotate-left"></i> 26+ Years Craft</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/chef_pastaio.jpg" alt="Master pastaio dusting semolina over handmade pasta"
              onerror="this.src='images/chef_rolling.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-award"></i>
              <span>Maestro Giancarlo De Luca<br><small>Founder &amp; Master Sfoglino</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-heart" style="color:var(--tomato-red);"></i>
              <span>Generational Emilian Atelier</span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">1998</span>
              <span class="hsb-label">Founded</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">0.6<small>mm</small></span>
              <span class="hsb-label">Sfoglia Thin</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">&lt;40<small>&deg;C</small></span>
              <span class="hsb-label">Slow Cold Air</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

    "products.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="page-hero" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/hero_products.jpg" class="hero-bg-img" alt="Fresh artisan pasta shapes and flour"
        onerror="this.src='images/bowl_dish_2.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <span>Pasta &amp; Deli Products</span>
        </nav>
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Il Negozio &bull; Fresh &amp; Dry Varieties</span>
        </div>
        <h1>Artisanal Pasta &amp; <br><em class="hero-italic-accent">Italian Deli Pantry</em></h1>
        <p class="hero-desc">Every pasta cut below is prepared by hand in our atelier using 100% Altamura durum semolina. Available in chilled fresh trays, bronze-drawn pantry cuts, and D.O.P. accompaniments.</p>
        <div class="hero-cta-row">
          <a href="#productsGrid" class="hero-cta-primary">
            <span>Browse All Cuts</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <a href="catering.html" class="hero-cta-ghost">Catering Platters</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-box"></i> Insulated Thermal Packing</div>
          <div class="htr-item"><i class="fa-solid fa-truck-fast"></i> Same-Day Dispatch</div>
          <div class="htr-item"><i class="fa-solid fa-utensils"></i> 18+ Daily Shapes</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/prod_pappardelle.jpg" alt="Handmade pasta selection"
              onerror="this.src='images/bowl_dish_1.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-fire-burner"></i>
              <span>Bronze Die Extruded<br><small>Porous Sauce Grip</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-star"></i>
              <span>4.9 / 5.0 <em>(Patrons Favorite)</em></span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">18<small>+</small></span>
              <span class="hsb-label">Pasta Shapes</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">100<small>%</small></span>
              <span class="hsb-label">Altamura Wheat</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">4<small>&deg;C</small></span>
              <span class="hsb-label">Chilled Packing</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

    "catering.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="catering-hero-section" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/catering_spread.jpg" class="hero-bg-img" alt="Spectacular Italian banquet catering spread"
        onerror="this.src='images/italian_dining.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <span>Catering Orders &amp; Feasts</span>
        </nav>
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Banchetti &amp; Ricevimenti &bull; Turnkey Hospitality</span>
        </div>
        <h1>Authentic Italian Feasts for <br><em class="hero-italic-accent">Memorable Celebrations</em></h1>
        <p class="hero-desc">Steaming multi-layered lasagna pans, custom pasta bars, and monumental antipasti boards designed to feed groups of 10 to over 150 guests with flawless Italian warmth.</p>
        <div class="hero-cta-row">
          <a href="#catering-packages" class="hero-cta-primary">
            <span>Explore Packages</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <a href="#catering-form-section" class="hero-cta-ghost">Request Quote</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-users"></i> 10 to 150+ Guests</div>
          <div class="htr-item"><i class="fa-solid fa-fire-burner"></i> Delivered Hot in Warmers</div>
          <div class="htr-item"><i class="fa-solid fa-clock"></i> 24h Setup Notice</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/catering_spread.jpg" alt="Italian feast spread"
              onerror="this.src='images/kitchen.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-bell-concierge"></i>
              <span>Turnkey Catering<br><small>Buffet &amp; Chafing Sets</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-tag"></i>
              <span>Packages From $22 / Guest</span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">150<small>+</small></span>
              <span class="hsb-label">Max Capacity</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">24<small>h</small></span>
              <span class="hsb-label">Setup Notice</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">100<small>%</small></span>
              <span class="hsb-label">Hot Delivery</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

    "blog.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="page-hero" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/hero_blog.jpg" class="hero-bg-img" alt="Culinary journal and pasta making recipes"
        onerror="this.src='images/article_emulsion.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <span>Il Diario del Pastaio</span>
        </nav>
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Cucina &bull; Techniques &amp; Recipes</span>
        </div>
        <h1>The Pastaio's Journal &amp; <br><em class="hero-italic-accent">Culinary Guides</em></h1>
        <p class="hero-desc">Masterclasses in ancestral sfoglia rolling, emulsification science, trattoria sauce pairings, and seasonal Emilian secrets straight from our kitchen table.</p>
        <div class="hero-cta-row">
          <a href="#featured-article" class="hero-cta-primary">
            <span>Read Masterclass</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <a href="#articles-grid" class="hero-cta-ghost">All Guides</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-user-pen"></i> Master Pastaio Authored</div>
          <div class="htr-item"><i class="fa-solid fa-fire"></i> Trattoria Secrets</div>
          <div class="htr-item"><i class="fa-solid fa-book-open"></i> Weekly Dispatch</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/article_emulsion.jpg" alt="Chef tossing fresh pasta in pan"
              onerror="this.src='images/hero_noodle_lift.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-fire"></i>
              <span>Featured Masterclass<br><small>Starch Emulsion Science</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-lightbulb" style="color:var(--golden-yellow);"></i>
              <span>Liquid Gold Secret</span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">10<small>g</small></span>
              <span class="hsb-label">Salt Ratio</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">0<small>%</small></span>
              <span class="hsb-label">Cream Rule</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">4<small>min</small></span>
              <span class="hsb-label">Al Dente Boil</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

    "contact.html": """  <!-- =========================================================================
       SECTION 1: HERO — BALANCED CINEMATIC SPLIT (UNIFIED HEIGHT: 500PX)
       ========================================================================= -->
  <section class="page-hero" id="hero-section">
    <div class="hero-bg-layers">
      <div class="hero-bg-overlay"></div>
      <img src="images/hero_contact.jpg" class="hero-bg-img" alt="Bottega entrance and warm Italian deli"
        onerror="this.src='images/hanging_lamp.jpg'">
    </div>
    <div class="container hero-cinematic-inner">
      <div class="hero-left-column">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <span>Contattaci &amp; Bottega</span>
        </nav>
        <div class="hero-tag-line">
          <span class="hero-tag-dot"></span>
          <span>Bottega &bull; Via della Spiga 24</span>
        </div>
        <h1>We Welcome You to <br><em class="hero-italic-accent">Our Italian Bottega</em></h1>
        <p class="hero-desc">Whether stopping by for tonight’s fresh pasta cuts, reserving custom celebration catering, or asking Maestro Giancarlo for a recipe suggestion, our doors are open.</p>
        <div class="hero-cta-row">
          <a href="#map-section" class="hero-cta-primary">
            <span>Bottega Directions</span>
            <i class="fa-solid fa-location-dot"></i>
          </a>
          <a href="tel:+15558902123" class="hero-cta-ghost">Call (555) 890-2123</a>
        </div>
        <div class="hero-trust-row">
          <div class="htr-item"><i class="fa-solid fa-shop"></i> Mon&ndash;Sat 8am&ndash;7:30pm</div>
          <div class="htr-item"><i class="fa-solid fa-wheat-awn"></i> Fresh Batch Daily</div>
          <div class="htr-item"><i class="fa-solid fa-square-parking"></i> Market District Parking</div>
        </div>
      </div>
      <div class="hero-right-column">
        <div class="hero-card-showcase">
          <div class="hero-image-float">
            <img src="images/hanging_lamp.jpg" alt="Artisan Italian bottega counter with hanging lamp"
              onerror="this.src='images/italian_dining.jpg'">
            <div class="hero-float-badge">
              <i class="fa-solid fa-shop"></i>
              <span>Deli Counter Open<br><small>Via della Spiga 24</small></span>
            </div>
            <div class="hero-rating-pill">
              <i class="fa-solid fa-star"></i>
              <span>4.9 / 5.0 <em>(Bologna Spirit)</em></span>
            </div>
          </div>
          <div class="hero-stat-tower">
            <div class="hero-stat-block">
              <span class="hsb-number">8<small>am</small></span>
              <span class="hsb-label">Open Daily</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">6<small>days</small></span>
              <span class="hsb-label">Every Week</span>
            </div>
            <div class="hsb-divider"></div>
            <div class="hero-stat-block">
              <span class="hsb-number">100<small>%</small></span>
              <span class="hsb-label">Local Hospitality</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
}

# Update all 6 files
for filename, new_hero in HERO_HTML_MAP.items():
    filepath = os.path.join(WORKSPACE, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()
    
    if "hero-home-2" in c:
        start_tag = 'class="hero-home-2"'
    elif "catering-hero-section" in c:
        start_tag = 'class="catering-hero-section"'
    elif "page-hero" in c:
        start_tag = 'class="page-hero"'
    else:
        print(f"Error: No hero tag found in {filename}")
        continue
    
    idx = c.find(start_tag)
    comment_idx = c.rfind("<!--", 0, idx)
    end_sec_idx = c.find("</section>", idx) + len("</section>")
    
    updated_content = c[:comment_idx] + new_hero + c[end_sec_idx:]
    
    # Update cache-busting on stylesheet and script links to ?v=8
    updated_content = re.sub(r'href="css/style\.css(\?v=\d+)?"', 'href="css/style.css?v=8"', updated_content)
    updated_content = re.sub(r'href="css/about_redesign\.css(\?v=\d+)?"', 'href="css/about_redesign.css?v=8"', updated_content)
    updated_content = re.sub(r'href="css/home2_redesign\.css(\?v=\d+)?"', 'href="css/home2_redesign.css?v=8"', updated_content)
    updated_content = re.sub(r'href="css/redesign_sections\.css(\?v=\d+)?"', 'href="css/redesign_sections.css?v=8"', updated_content)
    updated_content = re.sub(r'src="js/main\.js(\?v=\d+)?"', 'src="js/main.js?v=8"', updated_content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Updated hero on {filename} successfully!")

# Also cache bust index.html to ?v=8
index_path = os.path.join(WORKSPACE, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()
idx_content = re.sub(r'href="css/style\.css(\?v=\d+)?"', 'href="css/style.css?v=8"', idx_content)
idx_content = re.sub(r'href="css/redesign_sections\.css(\?v=\d+)?"', 'href="css/redesign_sections.css?v=8"', idx_content)
idx_content = re.sub(r'src="js/main\.js(\?v=\d+)?"', 'src="js/main.js?v=8"', idx_content)
with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated cache-busting on index.html to ?v=8!")

# UNIFIED HERO CSS RULES
UNIFIED_HERO_CSS = """
/* ==========================================================================
   UNIFIED HERO ENGINE (HOME 1 TO CONTACT) — EXACT MATCH TO HOME PAGE HEIGHT
   Every single page hero has min-height: 480px, max-height: 560px, height: 500px,
   display: flex, align-items: center, with the 2-column cinematic split.
   ========================================================================== */

.hero-home-1,
.hero-home-2,
.page-hero,
.catering-hero-section {
  position: relative !important;
  height: 500px !important;
  min-height: 480px !important;
  max-height: 560px !important;
  display: flex !important;
  align-items: center !important;
  padding: 2.25rem 0 2.5rem !important;
  background-color: var(--navy-dark) !important;
  color: var(--pure-white) !important;
  overflow: hidden !important;
  border-bottom: 2px solid var(--golden-yellow) !important;
  text-align: left !important;
}

.hero-bg-layers {
  position: absolute !important;
  inset: 0 !important;
  z-index: 1 !important;
}

.hero-bg-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  opacity: 0.22 !important;
  filter: saturate(1.1) !important;
}

.hero-bg-overlay {
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(90deg, rgba(4,18,51,0.95) 0%, rgba(6,26,70,0.86) 55%, rgba(6,26,70,0.68) 100%) !important;
  z-index: 2 !important;
}

.hero-cinematic-inner {
  position: relative !important;
  z-index: 5 !important;
  display: grid !important;
  grid-template-columns: 1.15fr 0.85fr !important;
  gap: 2.5rem !important;
  align-items: center !important;
  width: 100% !important;
}

.hero-left-column {
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
}

.hero-left-column .breadcrumb-nav {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  font-size: 0.78rem !important;
  color: rgba(255, 255, 255, 0.65) !important;
  margin-bottom: 0.45rem !important;
}

.hero-left-column .breadcrumb-nav a {
  color: var(--golden-yellow) !important;
  text-decoration: none !important;
}

.hero-tag-line {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  background: rgba(232, 184, 63, 0.15) !important;
  border: 1px solid rgba(232, 184, 63, 0.35) !important;
  color: var(--golden-yellow) !important;
  padding: 0.3rem 0.85rem !important;
  border-radius: 999px !important;
  font-size: 0.76rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  margin-bottom: 0.75rem !important;
  width: fit-content !important;
}

.hero-tag-dot {
  width: 6px !important;
  height: 6px !important;
  border-radius: 50% !important;
  background: var(--golden-yellow) !important;
  box-shadow: 0 0 8px var(--golden-yellow) !important;
}

.hero-left-column h1 {
  font-family: var(--font-serif) !important;
  font-size: clamp(2rem, 3.4vw, 2.85rem) !important;
  font-weight: 800 !important;
  color: var(--pure-white) !important;
  line-height: 1.12 !important;
  margin-bottom: 0.65rem !important;
}

.hero-italic-accent {
  font-style: italic !important;
  font-weight: 400 !important;
  color: var(--golden-yellow) !important;
}

.hero-desc {
  font-size: 0.92rem !important;
  line-height: 1.58 !important;
  color: rgba(255, 255, 255, 0.85) !important;
  max-width: 530px !important;
  margin-bottom: 1.25rem !important;
}

.hero-cta-row {
  display: flex !important;
  align-items: center !important;
  gap: 1rem !important;
  margin-bottom: 1.25rem !important;
}

.hero-cta-primary {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.6rem !important;
  background: linear-gradient(135deg, var(--golden-yellow) 0%, #d89b1c 100%) !important;
  color: var(--navy-dark) !important;
  font-weight: 700 !important;
  font-size: 0.88rem !important;
  padding: 0.7rem 1.35rem !important;
  border-radius: 50px !important;
  text-decoration: none !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 4px 14px rgba(232, 184, 63, 0.35) !important;
}

.hero-cta-primary:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 18px rgba(232, 184, 63, 0.5) !important;
  color: var(--navy-dark) !important;
}

.hero-cta-ghost {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.65rem 1.25rem !important;
  border-radius: 50px !important;
  border: 1px solid rgba(255, 255, 255, 0.35) !important;
  color: var(--pure-white) !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  text-decoration: none !important;
  transition: all 0.3s ease !important;
}

.hero-cta-ghost:hover {
  background: rgba(255, 255, 255, 0.1) !important;
  border-color: var(--pure-white) !important;
}

.hero-trust-row {
  display: flex !important;
  align-items: center !important;
  gap: 1.25rem !important;
  padding-top: 0.85rem !important;
  border-top: 1px solid rgba(255, 255, 255, 0.12) !important;
}

.htr-item {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.4rem !important;
  font-size: 0.76rem !important;
  color: rgba(255, 255, 255, 0.85) !important;
  font-weight: 600 !important;
}

.htr-item i {
  color: var(--golden-yellow) !important;
}

.hero-right-column {
  position: relative !important;
}

.hero-card-showcase {
  background: rgba(6, 26, 70, 0.75) !important;
  backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(232, 184, 63, 0.35) !important;
  border-radius: 20px !important;
  padding: 0.85rem !important;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4) !important;
}

.hero-image-float {
  position: relative !important;
  border-radius: 14px !important;
  overflow: hidden !important;
  height: 250px !important;
}

.hero-image-float img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
}

.hero-float-badge {
  position: absolute !important;
  top: 10px !important;
  left: 10px !important;
  background: rgba(4, 18, 51, 0.88) !important;
  backdrop-filter: blur(8px) !important;
  border: 1px solid rgba(232, 184, 63, 0.4) !important;
  padding: 0.35rem 0.65rem !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  color: var(--golden-yellow) !important;
  font-size: 0.76rem !important;
  font-weight: 700 !important;
  line-height: 1.15 !important;
  z-index: 2 !important;
}

.hero-float-badge small {
  color: rgba(255, 255, 255, 0.75) !important;
  font-weight: 500 !important;
  font-size: 0.66rem !important;
}

.hero-rating-pill {
  position: absolute !important;
  bottom: 10px !important;
  right: 10px !important;
  background: rgba(4, 18, 51, 0.92) !important;
  border: 1px solid rgba(232, 184, 63, 0.3) !important;
  padding: 0.25rem 0.65rem !important;
  border-radius: 50px !important;
  font-size: 0.74rem !important;
  font-weight: 700 !important;
  color: var(--golden-yellow) !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.35rem !important;
  z-index: 2 !important;
}

.hero-rating-pill em {
  font-style: normal !important;
  color: rgba(255, 255, 255, 0.7) !important;
  font-weight: 400 !important;
}

.hero-stat-tower {
  display: grid !important;
  grid-template-columns: 1fr auto 1fr auto 1fr !important;
  align-items: center !important;
  gap: 0.5rem !important;
  padding: 0.75rem 0.5rem 0.25rem !important;
}

.hero-stat-block {
  text-align: center !important;
}

.hsb-number {
  font-family: var(--font-serif) !important;
  font-size: 1.35rem !important;
  font-weight: 800 !important;
  color: var(--golden-yellow) !important;
  display: block !important;
  line-height: 1 !important;
}

.hsb-number small {
  font-size: 0.75rem !important;
  font-weight: 600 !important;
  color: var(--pure-white) !important;
  margin-left: 2px !important;
}

.hsb-label {
  font-size: 0.68rem !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.04em !important;
  color: rgba(255, 255, 255, 0.75) !important;
  display: block !important;
  margin-top: 3px !important;
}

.hsb-divider {
  width: 1px !important;
  height: 26px !important;
  background: rgba(255, 255, 255, 0.15) !important;
}

@media (max-width: 992px) {
  .hero-home-1,
  .hero-home-2,
  .page-hero,
  .catering-hero-section {
    height: auto !important;
    min-height: 480px !important;
    max-height: none !important;
    padding: 3rem 0 !important;
  }

  .hero-cinematic-inner {
    grid-template-columns: 1fr !important;
    gap: 2rem !important;
  }
}
"""

with open(STYLE_CSS, "r", encoding="utf-8") as f:
    style_content = f.read()

marker = "/* === UNIFIED HERO ENGINE (V8) === */"
if marker in style_content:
    style_content = style_content[:style_content.find(marker)]

style_content = style_content.strip() + "\n\n" + marker + "\n" + UNIFIED_HERO_CSS
with open(STYLE_CSS, "w", encoding="utf-8") as f:
    f.write(style_content)
print("style.css updated with UNIFIED_HERO_CSS at end!")
print("ALL UNIFIED HERO REDESIGNS COMPLETE!")
