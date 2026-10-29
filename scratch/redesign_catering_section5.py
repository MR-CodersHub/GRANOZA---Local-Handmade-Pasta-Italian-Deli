# -*- coding: utf-8 -*-
"""
Redesign Section 5 of catering.html (Eventi su Misura),
tighten all catering section paddings from 5.5rem to 3.25rem to eliminate excessive whitespace,
and add the interactive event tier selector in main.js.
"""
import os
import re

WORKSPACE = r"c:\Users\dines\OneDrive\Desktop\italian"
CATERING_HTML = os.path.join(WORKSPACE, "catering.html")
STYLE_CSS = os.path.join(WORKSPACE, "css", "style.css")
MAIN_JS = os.path.join(WORKSPACE, "js", "main.js")

# 1. NEW SECTION 5 HTML FOR CATERING.HTML
CATERING_EVENTS_NEW_HTML = """  <!-- =========================================================================
       SECTION 5: CELEBRATIONS, WEDDINGS & CORPORATE EVENTS (BESPOKE ATELIER REDESIGN)
       ========================================================================= -->
  <section class="catering-events-section" id="catering-occasions">
    <div class="container">
      <div class="section-header">
        <span class="eyebrow eyebrow-gold"><i class="fa-solid fa-calendar-check"></i> Eventi su Misura</span>
        <h2>Tailored for Every <em>Milestone &amp; Gathering</em></h2>
        <div class="gold-divider"><i class="fa-solid fa-heart"></i></div>
        <p>From intimate family banquets to 150-guest corporate galas, our atelier crafts authentic Emilian feasts with hot chafing warmers, dedicated pastai, and turnkey Italian hospitality.</p>
      </div>

      <div class="occasions-cards-grid">
        <!-- Occasion 1: Family Gatherings -->
        <article class="occ-card">
          <div class="occ-media">
            <img src="images/italian_dining.jpg" alt="Italian family sharing dinner around a warm table" onerror="this.src='images/bowl_dish_1.jpg'">
            <span class="occ-tag"><i class="fa-solid fa-people-roof"></i> Famiglia &amp; Tradizione</span>
            <span class="occ-capacity-pill"><i class="fa-solid fa-users"></i> 10 &ndash; 45 Guests</span>
          </div>
          <div class="occ-body">
            <h3>Family Gatherings &amp; Milestones</h3>
            <span class="occ-sub">Sunday Lunches, Baptisms &amp; Anniversaries</span>
            <p>Generous, multi-layered warm lasagna trays, platters of hand-pinched ravioli, and house-made tiramisù that bring multiple generations around the table in celebration.</p>
            <div class="occ-perks">
              <span><i class="fa-solid fa-check"></i> Family-style ceramic-look warmers</span>
              <span><i class="fa-solid fa-check"></i> Rosemary focaccia &amp; Parmigiano included</span>
            </div>
            <div class="occ-footer">
              <a href="#catering-form-section" class="occ-link-btn" onclick="selectEventTier('sunday', 'Family Milestone Gathering')">
                <span>Inquire For Family Feast</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </article>

        <!-- Occasion 2: Corporate Luncheons -->
        <article class="occ-card">
          <div class="occ-media">
            <img src="images/hero_products.jpg" alt="Italian pasta buffet catering display" onerror="this.src='images/kitchen.jpg'">
            <span class="occ-tag"><i class="fa-solid fa-briefcase"></i> Executive &amp; Corporate</span>
            <span class="occ-capacity-pill"><i class="fa-solid fa-users"></i> 15 &ndash; 120 Guests</span>
          </div>
          <div class="occ-body">
            <h3>Corporate Luncheons &amp; Summits</h3>
            <span class="occ-sub">Board Meetings, Client Lunches &amp; Galas</span>
            <p>Punctual, seamless hot delivery with individual bowls or buffet chafing stations, clear dietary markings, and eco-friendly tableware for effortless corporate polish.</p>
            <div class="occ-perks">
              <span><i class="fa-solid fa-check"></i> Guaranteed on-time thermal hot delivery</span>
              <span><i class="fa-solid fa-check"></i> Gluten-aware, vegan &amp; allergen labels</span>
            </div>
            <div class="occ-footer">
              <a href="#catering-form-section" class="occ-link-btn" onclick="selectEventTier('pranzo', 'Corporate Luncheon')">
                <span>Inquire For Corporate</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </article>

        <!-- Occasion 3: Weddings & Rehearsals (Featured Card!) -->
        <article class="occ-card occ-card-featured">
          <div class="occ-featured-badge"><i class="fa-solid fa-crown"></i> Signature Experience</div>
          <div class="occ-media">
            <img src="images/catering_spread.jpg" alt="Grand wedding catering spread with pasta, antipasti and wine" onerror="this.src='images/italian_dining.jpg'">
            <span class="occ-tag"><i class="fa-solid fa-ring"></i> Nozze &amp; Ricevimenti</span>
            <span class="occ-capacity-pill"><i class="fa-solid fa-users"></i> 40 &ndash; 200+ Guests</span>
          </div>
          <div class="occ-body">
            <h3>Weddings &amp; Rustic Rehearsals</h3>
            <span class="occ-sub">Rehearsal Dinners &amp; Elegant Receptions</span>
            <p>Create an unforgettable theatrical spectacle with our dedicated live Pastaio station, tossing hot pasta in a 40kg wheel of 30-month Parmigiano Reggiano before your guests.</p>
            <div class="occ-perks">
              <span><i class="fa-solid fa-check"></i> Live Parmigiano wheel show station</span>
              <span><i class="fa-solid fa-check"></i> Dedicated chef &amp; Italian sommelier pairing</span>
            </div>
            <div class="occ-footer">
              <a href="#catering-form-section" class="occ-link-btn occ-btn-gold" onclick="selectEventTier('grand', 'Wedding & Rehearsal Dinner')">
                <span>Book Wedding Experience</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </article>

        <!-- Occasion 4: Cocktail Parties -->
        <article class="occ-card">
          <div class="occ-media">
            <img src="images/deli_charcuterie.jpg" alt="Artisan Italian charcuterie and antipasti display board" onerror="this.src='images/hanging_lamp.jpg'">
            <span class="occ-tag"><i class="fa-solid fa-champagne-glasses"></i> Aperitivo &amp; Soirée</span>
            <span class="occ-capacity-pill"><i class="fa-solid fa-users"></i> 20 &ndash; 100 Guests</span>
          </div>
          <div class="occ-body">
            <h3>Aperitivo &amp; Cocktail Soirées</h3>
            <span class="occ-sub">Private Receptions &amp; Holiday Galas</span>
            <p>Monumental wooden antipasti boards laden with 24-month Prosciutto di Parma, bite-sized truffle arancini, crispy frico, and artisanal finger foods perfect for mingling.</p>
            <div class="occ-perks">
              <span><i class="fa-solid fa-check"></i> Carved salumi &amp; cave-aged cheeses</span>
              <span><i class="fa-solid fa-check"></i> Passed warm bite-sized arancini &amp; skewers</span>
            </div>
            <div class="occ-footer">
              <a href="#catering-form-section" class="occ-link-btn" onclick="selectEventTier('classic', 'Cocktail Soirée & Aperitivo')">
                <span>Inquire For Cocktail Party</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </article>
      </div>

      <!-- Reassurance Concierge Strip -->
      <div class="occ-concierge-strip">
        <div class="ocs-item">
          <i class="fa-solid fa-phone-volume"></i>
          <div>
            <strong>Dedicated Catering Concierge</strong>
            <span>Direct: <a href="tel:+15558902123" style="color:var(--golden-yellow); font-weight:700;">(555) 890-2123</a> &bull; catering@granoza.com</span>
          </div>
        </div>
        <div class="ocs-divider"></div>
        <div class="ocs-item">
          <i class="fa-solid fa-stopwatch"></i>
          <div>
            <strong>Express 24-Hour Confirmation</strong>
            <span>Custom proposal and dietary consultation within 1 business day</span>
          </div>
        </div>
        <div class="ocs-divider"></div>
        <div class="ocs-action">
          <a href="#catering-form-section" class="btn btn-gold btn-sm">
            <i class="fa-solid fa-calculator"></i> Build Instant Estimate
          </a>
        </div>
      </div>
    </div>
  </section>"""

# 2. UPDATE CATERING.HTML
with open(CATERING_HTML, "r", encoding="utf-8") as f:
    cat_content = f.read()

# Replace section 5
pattern = r"<!-- =========================================================================\s+SECTION 5: CELEBRATIONS, WEDDINGS & CORPORATE EVENTS.*?<!-- =========================================================================\s+SECTION 6:"
match = re.search(pattern, cat_content, flags=re.DOTALL)
if match:
    replacement = CATERING_EVENTS_NEW_HTML + "\n\n  <!-- =========================================================================\n       SECTION 6:"
    cat_content = cat_content[:match.start()] + replacement + cat_content[match.end():]
    print("Section 5 replaced successfully in catering.html!")
else:
    print("WARNING: Pattern not found for Section 5! Searching alternative...")
    sec5_start = cat_content.find('class="catering-events-section"')
    comment5_start = cat_content.rfind('<!--', 0, sec5_start)
    sec6_start = cat_content.find('class="catering-instructions-section"')
    comment6_start = cat_content.rfind('<!--', 0, sec6_start)
    cat_content = cat_content[:comment5_start] + CATERING_EVENTS_NEW_HTML + "\n\n" + cat_content[comment6_start:]
    print("Alternative replacement successful!")

# Ensure stylesheet version is ?v=7 for immediate cache-busting
cat_content = re.sub(r'href="css/style\.css(\?v=\d+)?"', 'href="css/style.css?v=7"', cat_content)
cat_content = re.sub(r'src="js/main\.js(\?v=\d+)?"', 'src="js/main.js?v=7"', cat_content)

with open(CATERING_HTML, "w", encoding="utf-8") as f:
    f.write(cat_content)
print("catering.html written with new Section 5 and cache-busting ?v=7.")

# 3. CSS RULES FOR THE REDESIGNED SECTION 5 AND PADDING TIGHTENING
CATERING_CSS_RULES = """
/* ==========================================================================
   CATERING SECTION 5 REDESIGN — EVENTI SU MISURA (V7)
   Eliminates the empty 4-box layout with rich photo cards, occasion tags,
   guest capacity pills, perks list, and interactive concierge bar.
   ========================================================================== */

.catering-events-section {
  padding: 3.25rem 0 !important;
  background-color: var(--warm-ivory) !important;
  border-top: 1px solid var(--beige-border) !important;
  border-bottom: 1px solid var(--beige-border) !important;
}

.catering-events-section .section-header {
  margin-bottom: 2rem !important;
}

.catering-events-section .section-header h2 {
  font-size: clamp(1.9rem, 2.8vw, 2.45rem) !important;
  margin-bottom: 0.35rem !important;
}

.catering-events-section .section-header h2 em {
  font-style: italic !important;
  color: var(--tomato-red) !important;
}

.occasions-cards-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 1.35rem !important;
  align-items: stretch !important;
}

.occ-card {
  background: var(--pure-white) !important;
  border: 1px solid var(--beige-border) !important;
  border-radius: 16px !important;
  overflow: hidden !important;
  display: flex !important;
  flex-direction: column !important;
  box-shadow: var(--shadow-sm) !important;
  transition: all 0.3s ease !important;
  position: relative !important;
}

.occ-card:hover {
  transform: translateY(-4px) !important;
  border-color: var(--golden-yellow) !important;
  box-shadow: var(--shadow-md) !important;
}

.occ-card-featured {
  border: 2px solid var(--golden-yellow) !important;
  box-shadow: 0 8px 24px rgba(232, 184, 63, 0.2) !important;
}

.occ-featured-badge {
  position: absolute !important;
  top: 10px !important;
  right: 10px !important;
  background: var(--golden-yellow) !important;
  color: var(--navy-dark) !important;
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  padding: 0.25rem 0.65rem !important;
  border-radius: 999px !important;
  z-index: 5 !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.3rem !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.04em !important;
}

.occ-media {
  position: relative !important;
  height: 160px !important;
  overflow: hidden !important;
}

.occ-media img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  transition: transform 0.4s ease !important;
}

.occ-card:hover .occ-media img {
  transform: scale(1.05) !important;
}

.occ-tag {
  position: absolute !important;
  top: 10px !important;
  left: 10px !important;
  background: rgba(4, 18, 51, 0.88) !important;
  backdrop-filter: blur(8px) !important;
  color: var(--golden-yellow) !important;
  font-size: 0.68rem !important;
  font-weight: 700 !important;
  padding: 0.25rem 0.6rem !important;
  border-radius: 999px !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.35rem !important;
  z-index: 2 !important;
}

.occ-capacity-pill {
  position: absolute !important;
  bottom: 10px !important;
  right: 10px !important;
  background: rgba(255, 255, 255, 0.95) !important;
  color: var(--navy-deep) !important;
  font-size: 0.7rem !important;
  font-weight: 700 !important;
  padding: 0.2rem 0.55rem !important;
  border-radius: 6px !important;
  box-shadow: var(--shadow-sm) !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.35rem !important;
  z-index: 2 !important;
}

.occ-body {
  padding: 1.25rem !important;
  display: flex !important;
  flex-direction: column !important;
  flex: 1 !important;
}

.occ-body h3 {
  font-family: var(--font-serif) !important;
  font-size: 1.15rem !important;
  color: var(--navy-deep) !important;
  margin: 0 0 0.25rem !important;
  line-height: 1.25 !important;
}

.occ-sub {
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  color: var(--tomato-red) !important;
  letter-spacing: 0.04em !important;
  display: block !important;
  margin-bottom: 0.65rem !important;
}

.occ-body p {
  font-size: 0.84rem !important;
  color: var(--text-dark) !important;
  line-height: 1.5 !important;
  margin: 0 0 0.85rem !important;
}

.occ-perks {
  display: flex !important;
  flex-direction: column !important;
  gap: 0.35rem !important;
  margin-bottom: 1rem !important;
  padding-top: 0.65rem !important;
  border-top: 1px dashed var(--beige-border) !important;
}

.occ-perks span {
  font-size: 0.74rem !important;
  font-weight: 600 !important;
  color: var(--navy-deep) !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.4rem !important;
}

.occ-perks i {
  color: #059669 !important;
  font-size: 0.72rem !important;
}

.occ-footer {
  margin-top: auto !important;
  padding-top: 0.75rem !important;
  border-top: 1px solid var(--beige-border) !important;
}

.occ-link-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  font-size: 0.8rem !important;
  font-weight: 700 !important;
  color: var(--navy-deep) !important;
  text-decoration: none !important;
  padding: 0.55rem 0.85rem !important;
  background: var(--warm-ivory) !important;
  border-radius: 8px !important;
  transition: all 0.2s ease !important;
}

.occ-link-btn:hover {
  background: var(--navy-deep) !important;
  color: var(--golden-yellow) !important;
}

.occ-btn-gold {
  background: var(--golden-yellow) !important;
  color: var(--navy-dark) !important;
  font-weight: 800 !important;
}

.occ-btn-gold:hover {
  background: #d89b1c !important;
  color: var(--navy-dark) !important;
}

/* Concierge Strip */
.occ-concierge-strip {
  margin-top: 2rem !important;
  background: var(--pure-white) !important;
  border: 1px solid var(--beige-border) !important;
  border-radius: 14px !important;
  padding: 1rem 1.5rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 1.5rem !important;
  box-shadow: var(--shadow-sm) !important;
}

.ocs-item {
  display: flex !important;
  align-items: center !important;
  gap: 0.75rem !important;
}

.ocs-item i {
  font-size: 1.4rem !important;
  color: var(--golden-yellow) !important;
}

.ocs-item strong {
  display: block !important;
  font-size: 0.82rem !important;
  color: var(--navy-deep) !important;
  line-height: 1.2 !important;
}

.ocs-item span {
  font-size: 0.74rem !important;
  color: var(--text-muted) !important;
}

.ocs-divider {
  width: 1px !important;
  height: 32px !important;
  background: var(--beige-border) !important;
}

/* Tighten all other catering sections */
.catering-hero-section {
  padding: 3rem 0 3.25rem !important;
}

.catering-packages-section {
  padding: 3.25rem 0 !important;
}

.catering-platters-section {
  padding: 3.25rem 0 !important;
}

.catering-instructions-section {
  padding: 3.25rem 0 !important;
}

.catering-form-section {
  padding: 3.25rem 0 !important;
}

@media (max-width: 1100px) {
  .occasions-cards-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.5rem !important;
  }

  .occ-concierge-strip {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 1rem !important;
  }

  .ocs-divider {
    display: none !important;
  }
}

@media (max-width: 600px) {
  .occasions-cards-grid {
    grid-template-columns: 1fr !important;
  }
}
"""

# 4. APPEND TO STYLE.CSS
with open(STYLE_CSS, "r", encoding="utf-8") as f:
    style_content = f.read()

marker = "/* === CATERING REDESIGN RULES (V7) === */"
if marker in style_content:
    style_content = style_content[:style_content.find(marker)]

style_content = style_content.strip() + "\n\n" + marker + "\n" + CATERING_CSS_RULES
with open(STYLE_CSS, "w", encoding="utf-8") as f:
    f.write(style_content)
print("style.css updated with CATERING_CSS_RULES at end!")

# 5. ADD selectEventTier FUNCTION TO MAIN.JS
with open(MAIN_JS, "r", encoding="utf-8") as f:
    js_content = f.read()

if "window.selectEventTier" not in js_content:
    tier_func = """
// Auto-select Catering Package and Event Notes from Occasion Cards
window.selectEventTier = function(tier, occasionName) {
  const pkgSelect = document.getElementById('catering_package');
  if (pkgSelect && tier) {
    pkgSelect.value = tier;
    if (typeof updateCateringEstimate === 'function') {
      updateCateringEstimate();
    }
  }
  const notesField = document.getElementById('catering_notes');
  if (notesField && occasionName) {
    if (!notesField.value.includes(occasionName)) {
      notesField.value = `Occasion: ${occasionName}. ` + notesField.value;
    }
  }
};
"""
    js_content = js_content.strip() + "\n" + tier_func
    with open(MAIN_JS, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("selectEventTier function added to main.js!")

# 6. UPDATE CACHE-BUSTING ON ALL HTML FILES TO ?v=7
import glob
for html_file in glob.glob(os.path.join(WORKSPACE, "*.html")):
    with open(html_file, "r", encoding="utf-8") as f:
        c = f.read()
    c = re.sub(r'href="css/style\.css(\?v=\d+)?"', 'href="css/style.css?v=7"', c)
    c = re.sub(r'src="js/main\.js(\?v=\d+)?"', 'src="js/main.js?v=7"', c)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(c)

print("All HTML files cache-busted with ?v=7!")
print("CATERING SECTION 5 REDESIGN COMPLETE!")
