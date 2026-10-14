/**
 * GRANOZA — Master JavaScript Logic
 * Local Handmade Pasta & Italian Deli
 * Pure Vanilla JavaScript — Zero Frameworks
 */

(function () {
  'use strict';

  // -------------------------------------------------------------
  // 1. CART STATE & LOCAL STORAGE ENGINE
  // -------------------------------------------------------------
  const CART_STORAGE_KEY = 'granoza_cart';

  function getCart() {
    try {
      const stored = localStorage.getItem(CART_STORAGE_KEY);
      return stored ? JSON.parse(stored) : [];
    } catch (e) {
      console.error('Failed to parse cart:', e);
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
      updateCartUI();
    } catch (e) {
      console.error('Failed to save cart:', e);
    }
  }

  function addToCart(item) {
    const cart = getCart();
    // Unique ID can be item.id or item.name + item.portion
    const itemKey = `${item.id || item.title}_${item.portion || 'standard'}`;
    const existingIndex = cart.findIndex(c => c.key === itemKey);

    if (existingIndex > -1) {
      cart[existingIndex].qty += (item.qty || 1);
    } else {
      cart.push({
        key: itemKey,
        id: item.id || Date.now().toString(),
        title: item.title,
        price: parseFloat(item.price),
        portion: item.portion || '500g Fresh Pack',
        image: item.image || 'images/prod_tagliatelle.jpg',
        qty: item.qty || 1
      });
    }

    saveCart(cart);
    showToast(`Added "${item.title}" to your order basket!`, 'success');
  }

  function updateItemQty(key, delta) {
    let cart = getCart();
    const item = cart.find(c => c.key === key);
    if (!item) return;

    item.qty += delta;
    if (item.qty <= 0) {
      cart = cart.filter(c => c.key !== key);
      showToast(`Removed from order.`, 'info');
    }
    saveCart(cart);
  }

  function removeItem(key) {
    let cart = getCart();
    cart = cart.filter(c => c.key !== key);
    saveCart(cart);
    showToast(`Item removed from basket.`, 'info');
  }

  function clearCart() {
    saveCart([]);
    showToast('Your order basket has been cleared.', 'info');
  }

  function updateCartUI() {
    const cart = getCart();
    const totalQty = cart.reduce((acc, curr) => acc + curr.qty, 0);
    const subtotal = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

    // Update badges
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
      badge.textContent = totalQty;
      badge.style.display = totalQty > 0 ? 'flex' : 'none';
    });

    // Update drawer list
    const itemsList = document.querySelector('.cart-items-container');
    const subtotalEl = document.querySelector('.cart-subtotal-amount');

    if (subtotalEl) {
      subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
    }

    if (itemsList) {
      if (cart.length === 0) {
        itemsList.innerHTML = `
          <div class="cart-empty-state">
            <i class="fa-solid fa-basket-shopping"></i>
            <h4>Your Basket is Empty</h4>
            <p>Explore our fresh pasta varieties and artisanal deli selections to begin.</p>
            <a href="products.html" class="btn btn-primary btn-sm" style="margin-top: 1rem;">Browse Pasta</a>
          </div>
        `;
      } else {
        itemsList.innerHTML = cart.map(item => `
          <div class="cart-item" data-key="${item.key}">
            <img src="${item.image}" alt="${item.title}" class="cart-item-img" onerror="this.src='images/prod_tagliatelle.jpg'">
            <div class="cart-item-info">
              <h4>${item.title}</h4>
              <span class="cart-item-weight">${item.portion}</span>
              <div class="cart-item-price">$${(item.price * item.qty).toFixed(2)}</div>
            </div>
            <div class="cart-item-actions">
              <div class="qty-control">
                <button type="button" class="qty-btn btn-qty-minus" data-key="${item.key}">-</button>
                <span class="qty-val">${item.qty}</span>
                <button type="button" class="qty-btn btn-qty-plus" data-key="${item.key}">+</button>
              </div>
              <button type="button" class="cart-remove-btn btn-remove-item" data-key="${item.key}" title="Remove item">
                <i class="fa-regular fa-trash-can"></i>
              </button>
            </div>
          </div>
        `).join('');

        // Attach listeners
        itemsList.querySelectorAll('.btn-qty-minus').forEach(btn => {
          btn.addEventListener('click', () => updateItemQty(btn.dataset.key, -1));
        });
        itemsList.querySelectorAll('.btn-qty-plus').forEach(btn => {
          btn.addEventListener('click', () => updateItemQty(btn.dataset.key, 1));
        });
        itemsList.querySelectorAll('.btn-remove-item').forEach(btn => {
          btn.addEventListener('click', () => removeItem(btn.dataset.key));
        });
      }
    }
  }

  // -------------------------------------------------------------
  // 2. DRAWER & MODAL TOGGLES
  // -------------------------------------------------------------
  function setupDrawers() {
    const cartToggleBtns = document.querySelectorAll('.cart-toggle-btn');
    const cartDrawer = document.querySelector('.cart-drawer');
    const cartCloseBtn = document.querySelector('.cart-close-btn');
    const overlay = document.querySelector('.mobile-nav-overlay');

    const hamburgerBtn = document.querySelector('.hamburger-btn');
    const mobileDrawer = document.querySelector('.mobile-nav-drawer');
    const mobileCloseBtn = document.querySelector('.mobile-nav-close');

    function openCart() {
      if (cartDrawer) cartDrawer.classList.add('open');
      if (overlay) overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeCart() {
      if (cartDrawer) cartDrawer.classList.remove('open');
      if (overlay && (!mobileDrawer || !mobileDrawer.classList.contains('open'))) {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    }

    function openMobileNav() {
      if (mobileDrawer) mobileDrawer.classList.add('open');
      if (hamburgerBtn) hamburgerBtn.classList.add('active');
      if (overlay) overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeMobileNav() {
      if (mobileDrawer) mobileDrawer.classList.remove('open');
      if (hamburgerBtn) hamburgerBtn.classList.remove('active');
      if (overlay && (!cartDrawer || !cartDrawer.classList.contains('open'))) {
        overlay.classList.remove('open');
        document.body.style.overflow = '';
      }
    }

    cartToggleBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openCart();
      });
    });

    if (cartCloseBtn) cartCloseBtn.addEventListener('click', closeCart);
    if (hamburgerBtn) hamburgerBtn.addEventListener('click', openMobileNav);
    if (mobileCloseBtn) mobileCloseBtn.addEventListener('click', closeMobileNav);

    if (overlay) {
      overlay.addEventListener('click', () => {
        closeCart();
        closeMobileNav();
        closeModals();
      });
    }

    // Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeCart();
        closeMobileNav();
        closeModals();
      }
    });

    // Checkout Enquiry Modal Trigger from cart
    const checkoutBtn = document.querySelector('.btn-cart-checkout');
    if (checkoutBtn) {
      checkoutBtn.addEventListener('click', () => {
        const cart = getCart();
        if (cart.length === 0) {
          showToast('Please add items to your basket first.', 'error');
          return;
        }
        closeCart();
        openOrderModal();
      });
    }
  }

  // -------------------------------------------------------------
  // 3. HEADER SCROLL & ACTIVE PAGE HIGHLIGHT
  // -------------------------------------------------------------
  function setupHeader() {
    const header = document.querySelector('.main-header');
    const backToTop = document.querySelector('.back-to-top');

    window.addEventListener('scroll', () => {
      const scrollPos = window.scrollY;
      if (header) {
        if (scrollPos > 40) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      }

      if (backToTop) {
        if (scrollPos > 450) {
          backToTop.classList.add('visible');
        } else {
          backToTop.classList.remove('visible');
        }
      }
    });

    if (backToTop) {
      backToTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    // Set active link based on current page
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href === currentPath || (currentPath === '' && href === 'index.html')) {
        link.classList.add('active');
      }
    });
  }

  // -------------------------------------------------------------
  // 3B. THEME & RTL CONTROLS ENGINE
  // -------------------------------------------------------------
  const THEME_STORAGE_KEY = 'granoza_theme';
  const DIR_STORAGE_KEY = 'granoza_direction';

  function initThemeAndRTL() {
    // Read saved or attribute states
    const savedTheme = localStorage.getItem(THEME_STORAGE_KEY) ||
      document.documentElement.getAttribute('data-theme') || 'light';
    applyTheme(savedTheme, false);

    const savedDir = localStorage.getItem(DIR_STORAGE_KEY) ||
      document.documentElement.getAttribute('dir') || 'ltr';
    applyDirection(savedDir, false);

    // Bind all theme buttons (desktop header + mobile drawer)
    const themeButtons = document.querySelectorAll('.theme-toggle-btn');
    themeButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleTheme();
      });
    });

    // Bind all RTL buttons (desktop header + mobile drawer)
    const rtlButtons = document.querySelectorAll('.rtl-toggle-btn');
    rtlButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleDirection();
      });
    });
  }

  function applyTheme(theme, save = true) {
    document.documentElement.setAttribute('data-theme', theme);
    if (save) {
      try {
        localStorage.setItem(THEME_STORAGE_KEY, theme);
      } catch (e) {}
    }

    const themeButtons = document.querySelectorAll('.theme-toggle-btn');
    themeButtons.forEach(btn => {
      const icon = btn.querySelector('i');
      if (theme === 'dark') {
        if (icon) icon.className = 'fa-solid fa-sun';
        btn.setAttribute('title', 'Switch to Light Theme');
        btn.setAttribute('aria-label', 'Switch to Light Theme');
      } else {
        if (icon) icon.className = 'fa-solid fa-moon';
        btn.setAttribute('title', 'Switch to Dark Theme');
        btn.setAttribute('aria-label', 'Switch to Dark Theme');
      }
    });
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme, true);
    showToast(nextTheme === 'dark' ? 'Midnight Luxury Dark Theme enabled' : 'Artisanal Light Theme enabled', 'info');
  }

  function applyDirection(dir, save = true) {
    document.documentElement.setAttribute('dir', dir);
    if (save) {
      try {
        localStorage.setItem(DIR_STORAGE_KEY, dir);
      } catch (e) {}
    }

    const rtlButtons = document.querySelectorAll('.rtl-toggle-btn');
    rtlButtons.forEach(btn => {
      const textSpan = btn.querySelector('.rtl-text');
      if (dir === 'rtl') {
        if (textSpan) textSpan.textContent = 'LTR';
        btn.setAttribute('title', 'Switch to LTR (Left-to-Right) Layout');
        btn.setAttribute('aria-label', 'Switch to LTR (Left-to-Right) Layout');
        btn.classList.add('active');
      } else {
        if (textSpan) textSpan.textContent = 'RTL';
        btn.setAttribute('title', 'Switch to RTL (Right-to-Left) Layout');
        btn.setAttribute('aria-label', 'Switch to RTL (Right-to-Left) Layout');
        btn.classList.remove('active');
      }
    });
  }

  function toggleDirection() {
    const currentDir = document.documentElement.getAttribute('dir') === 'rtl' ? 'rtl' : 'ltr';
    const nextDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
    applyDirection(nextDir, true);
    showToast(nextDir === 'rtl' ? 'RTL Layout enabled' : 'LTR Layout enabled', 'info');
  }

  // -------------------------------------------------------------
  // 4. TOAST NOTIFICATION ENGINE
  // -------------------------------------------------------------
  function showToast(message, type = 'success') {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    let icon = 'fa-circle-check';
    if (type === 'error') icon = 'fa-triangle-exclamation';
    if (type === 'info') icon = 'fa-circle-info';

    toast.innerHTML = `
      <i class="fa-solid ${icon}"></i>
      <span>${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3800);
  }

  window.showToast = showToast; // Expose globally

  // -------------------------------------------------------------
  // 5. PRODUCTS FILTER & QUICK VIEW MODAL
  // -------------------------------------------------------------
  function setupProductsPage() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const productCards = document.querySelectorAll('.product-item-card');

    if (filterBtns.length > 0 && productCards.length > 0) {
      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const filter = btn.dataset.filter;
          productCards.forEach(card => {
            const category = card.dataset.category;
            if (filter === 'all' || category === filter) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          });
        });
      });
    }

    // Add to cart buttons on products and redesigned spotlight/board
    document.querySelectorAll('.btn-add-pasta').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.product-item-card') || 
                     btn.closest('.pasta-card') || 
                     btn.closest('.pbs-cell') || 
                     btn.closest('.pss-feature-hero') || 
                     btn.closest('.pdb-item');
        if (!card) return;

        const title = card.querySelector('h3, h5, .pasta-card-title')?.textContent.trim() || 'Fresh Pasta';
        const priceStr = card.querySelector('.product-price-tag, .pasta-card-price, .pbs-price, .pfh-val, .pdb-item-price')?.textContent.replace(/[^0-9.]/g, '') || '14.50';
        const img = card.querySelector('img')?.getAttribute('src') || 'images/prod_tagliatelle.jpg';
        const id = card.dataset.id || title.toLowerCase().replace(/\s+/g, '-');

        addToCart({
          id,
          title,
          price: parseFloat(priceStr),
          image: img,
          portion: '500g Fresh Pack'
        });
      });
    });

    // Quick View buttons
    document.querySelectorAll('.btn-quick-view').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.product-item-card');
        if (!card) return;

        const title = card.querySelector('h3')?.textContent.trim() || 'Handmade Pasta';
        const price = card.querySelector('.product-price-tag')?.innerHTML || '$14.00';
        const desc = card.querySelector('p')?.textContent.trim() || '';
        const img = card.querySelector('img')?.getAttribute('src') || 'images/prod_tagliatelle.jpg';
        const ingredients = card.querySelector('.product-ingredients-snippet')?.textContent.trim() || '100% Durum Wheat Semolina, Farm Fresh Eggs';
        const cookTime = card.querySelector('.product-cook-badge')?.textContent.trim() || '3-4 mins';

        openQuickViewModal({ title, price, desc, img, ingredients, cookTime });
      });
    });
  }

  function openQuickViewModal(data) {
    let modal = document.querySelector('.quickview-modal-overlay');
    if (!modal) {
      modal = document.createElement('div');
      modal.className = 'modal-overlay quickview-modal-overlay';
      modal.innerHTML = `
        <div class="modal-card">
          <button type="button" class="modal-close-btn">&times;</button>
          <div class="modal-media">
            <img src="${data.img}" alt="${data.title}" class="modal-img-el">
          </div>
          <div class="modal-body">
            <span class="eyebrow" style="margin-bottom:0.4rem;"><i class="fa-solid fa-wheat-awn"></i> Artisan Deli Selection</span>
            <h2 class="modal-title-el">${data.title}</h2>
            <div class="modal-price modal-price-el">${data.price}</div>
            <p class="modal-desc-el">${data.desc}</p>
            
            <div style="background:var(--warm-ivory); padding:0.85rem; border-radius:var(--radius-sm); margin-bottom:1.25rem; border-left:3px solid var(--golden-yellow);">
              <div style="font-size:0.78rem; font-weight:700; color:var(--tomato-red); text-transform:uppercase;">Ingredients & Semolina Origin</div>
              <div class="modal-ingr-el" style="font-size:0.85rem; color:var(--navy-deep); margin-top:0.25rem;">${data.ingredients}</div>
              <div style="font-size:0.8rem; color:var(--text-muted); margin-top:0.4rem;"><i class="fa-regular fa-clock" style="color:var(--golden-yellow);"></i> Recommended boil time: <strong>${data.cookTime}</strong> in rolling salted water.</div>
            </div>

            <div class="modal-portion-selector">
              <label>Select Fresh Pack Weight:</label>
              <div class="portion-options">
                <button type="button" class="portion-btn active" data-weight="500g" data-multiplier="1">500g (Serves 2-3)</button>
                <button type="button" class="portion-btn" data-weight="1kg" data-multiplier="1.9">1kg Family Box</button>
                <button type="button" class="portion-btn" data-weight="250g" data-multiplier="0.55">250g Single</button>
              </div>
            </div>

            <button type="button" class="btn btn-primary btn-modal-add" style="margin-top:auto;">
              <i class="fa-solid fa-basket-shopping"></i> Add to Order Basket
            </button>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      modal.querySelector('.modal-close-btn').addEventListener('click', closeModals);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModals();
      });

      // Portion click
      const portionBtns = modal.querySelectorAll('.portion-btn');
      portionBtns.forEach(pbtn => {
        pbtn.addEventListener('click', () => {
          portionBtns.forEach(b => b.classList.remove('active'));
          pbtn.classList.add('active');
        });
      });
    } else {
      // Update existing modal content
      modal.querySelector('.modal-img-el').src = data.img;
      modal.querySelector('.modal-title-el').textContent = data.title;
      modal.querySelector('.modal-price-el').innerHTML = data.price;
      modal.querySelector('.modal-desc-el').textContent = data.desc;
      modal.querySelector('.modal-ingr-el').textContent = data.ingredients;
    }

    // Setup Add to cart handler on modal
    const addBtn = modal.querySelector('.btn-modal-add');
    addBtn.onclick = () => {
      const activePortion = modal.querySelector('.portion-btn.active')?.dataset.weight || '500g';
      const cleanPrice = parseFloat(data.price.replace(/[^0-9.]/g, '')) || 14.50;
      addToCart({
        title: data.title,
        price: cleanPrice,
        image: data.img,
        portion: `${activePortion} Fresh Pack`
      });
      closeModals();
    };

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModals() {
    document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('open'));
    document.body.style.overflow = '';
  }

  // -------------------------------------------------------------
  // 6. ORDER ENQUIRY MODAL (FROM CART)
  // -------------------------------------------------------------
  function openOrderModal() {
    let modal = document.querySelector('.order-enquiry-modal');
    const cart = getCart();
    const subtotal = cart.reduce((acc, curr) => acc + (curr.price * curr.qty), 0);

    const itemsSummary = cart.map(i => `${i.qty}x ${i.title} (${i.portion})`).join(', ');

    if (!modal) {
      modal = document.createElement('div');
      modal.className = 'modal-overlay order-enquiry-modal';
      modal.innerHTML = `
        <div class="modal-card" style="max-width: 680px; grid-template-columns: 1fr;">
          <button type="button" class="modal-close-btn">&times;</button>
          <div class="modal-body" style="padding: 2.5rem;">
            <span class="eyebrow"><i class="fa-solid fa-bell-concierge"></i> Local Deli Pickup & Delivery</span>
            <h2>Complete Your Pasta Order</h2>
            <p>Review your selected items below and provide pickup details. Our pasta masters will prepare your fresh batch according to your scheduled time.</p>
            
            <div style="background:var(--warm-ivory); border:1px solid var(--beige-border); border-radius:var(--radius-md); padding:1rem 1.25rem; margin-bottom:1.5rem;">
              <div style="font-size:0.8rem; font-weight:700; color:var(--navy-deep); text-transform:uppercase;">Order Items:</div>
              <div class="order-summary-text" style="font-size:0.88rem; color:var(--text-dark); margin-top:0.3rem;">${itemsSummary}</div>
              <div style="font-size:1.15rem; font-weight:800; color:var(--tomato-red); margin-top:0.6rem; border-top:1px dashed var(--beige-border); padding-top:0.4rem;">
                Estimated Total: $${subtotal.toFixed(2)}
              </div>
            </div>

            <form class="order-enquiry-form">
              <div class="form-grid-2">
                <div class="form-group">
                  <label>Full Name <span>*</span></label>
                  <input type="text" class="form-control" name="order_name" required placeholder="e.g. Marco Rossi">
                </div>
                <div class="form-group">
                  <label>Phone Number <span>*</span></label>
                  <input type="tel" class="form-control" name="order_phone" required placeholder="e.g. (555) 234-5678">
                </div>
              </div>
              <div class="form-grid-2">
                <div class="form-group">
                  <label>Email Address <span>*</span></label>
                  <input type="email" class="form-control" name="order_email" required placeholder="e.g. marco@example.com">
                </div>
                <div class="form-group">
                  <label>Pickup / Delivery Date <span>*</span></label>
                  <input type="date" class="form-control" name="order_date" required>
                </div>
              </div>
              <div class="form-group" style="margin-bottom: 1.5rem;">
                <label>Special Instructions (Dietary, Allergy, Sauce Pairings)</label>
                <textarea class="form-control" name="order_notes" placeholder="e.g. Please dust pasta lightly with semolina; egg-free requested if available."></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-lg" style="width:100%;">
                <i class="fa-solid fa-circle-check"></i> Confirm Fresh Pasta Reservation
              </button>
            </form>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      modal.querySelector('.modal-close-btn').addEventListener('click', closeModals);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModals();
      });

      const form = modal.querySelector('.order-enquiry-form');
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = form.querySelector('[name="order_name"]').value;
        clearCart();
        closeModals();
        showToast(`Grazie, ${name}! Your order reservation has been confirmed.`, 'success');
      });
    } else {
      modal.querySelector('.order-summary-text').textContent = itemsSummary;
      modal.querySelector('.order-summary-text + div').textContent = `Estimated Total: $${subtotal.toFixed(2)}`;
    }

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  // -------------------------------------------------------------
  // 7. CATERING COST ESTIMATOR & FORM VALIDATION (`catering.html`)
  // -------------------------------------------------------------
  function setupCateringPage() {
    const guestInput = document.querySelector('[name="catering_guests"]');
    const packageSelect = document.querySelector('[name="catering_package"]');
    const costDisplay = document.querySelector('.cost-preview-amount');
    const cateringForm = document.querySelector('#cateringEnquiryForm');

    const packageRates = {
      'classic': 26,     // per guest
      'pranzo': 22,
      'sunday': 34,
      'grand': 42
    };

    function updateEstimatedCost() {
      if (!costDisplay || !guestInput || !packageSelect) return;
      const guests = parseInt(guestInput.value, 10) || 20;
      const pkg = packageSelect.value || 'classic';
      const rate = packageRates[pkg] || 26;
      const total = guests * rate;
      costDisplay.textContent = `$${total.toLocaleString()}`;
    }

    if (guestInput) guestInput.addEventListener('input', updateEstimatedCost);
    if (packageSelect) packageSelect.addEventListener('change', updateEstimatedCost);

    if (cateringForm) {
      cateringForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let isValid = true;

        const nameInput = cateringForm.querySelector('[name="catering_name"]');
        const emailInput = cateringForm.querySelector('[name="catering_email"]');
        const phoneInput = cateringForm.querySelector('[name="catering_phone"]');
        const dateInput = cateringForm.querySelector('[name="catering_date"]');

        [nameInput, emailInput, phoneInput, dateInput].forEach(inp => {
          if (!inp) return;
          const group = inp.closest('.form-group');
          if (!inp.value.trim()) {
            if (group) group.classList.add('has-error');
            isValid = false;
          } else {
            if (group) group.classList.remove('has-error');
          }
        });

        // Email regex
        if (emailInput && emailInput.value) {
          const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(emailInput.value.trim())) {
            emailInput.closest('.form-group')?.classList.add('has-error');
            isValid = false;
          }
        }

        if (!isValid) {
          showToast('Please correct the highlighted fields in the catering form.', 'error');
          return;
        }

        showToast(`Grazie mille, ${nameInput.value}! Your catering enquiry has been received. Our events manager will contact you within 24 hours.`, 'success');
        cateringForm.reset();
        updateEstimatedCost();
      });
    }
  }

  // -------------------------------------------------------------
  // 8. CONTACT FORM & FAQ ACCORDION (`contact.html`)
  // -------------------------------------------------------------
  function setupContactPage() {
    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');

      if (question && answer) {
        question.addEventListener('click', () => {
          const isOpen = item.classList.contains('active');

          // Close others
          faqItems.forEach(other => {
            other.classList.remove('active');
            const otherAnswer = other.querySelector('.faq-answer');
            if (otherAnswer) otherAnswer.style.maxHeight = null;
          });

          if (!isOpen) {
            item.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + 'px';
          } else {
            item.classList.remove('active');
            answer.style.maxHeight = null;
          }
        });
      }
    });

    // Contact Form
    const contactForm = document.querySelector('#contactMainForm');
    if (contactForm) {
      contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let isValid = true;

        const nameInput = contactForm.querySelector('[name="contact_name"]');
        const emailInput = contactForm.querySelector('[name="contact_email"]');
        const messageInput = contactForm.querySelector('[name="contact_message"]');

        [nameInput, emailInput, messageInput].forEach(inp => {
          if (!inp) return;
          const group = inp.closest('.form-group');
          if (!inp.value.trim()) {
            if (group) group.classList.add('has-error');
            isValid = false;
          } else {
            if (group) group.classList.remove('has-error');
          }
        });

        if (emailInput && emailInput.value) {
          const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(emailInput.value.trim())) {
            emailInput.closest('.form-group')?.classList.add('has-error');
            isValid = false;
          }
        }

        if (!isValid) {
          showToast('Please complete all required fields.', 'error');
          return;
        }

        showToast(`Grazie, ${nameInput.value}! Your message has been delivered to our deli team.`, 'success');
        contactForm.reset();
      });
    }
  }

  // -------------------------------------------------------------
  // 9. BLOG PAGE READER MODAL & FILTER (`blog.html`)
  // -------------------------------------------------------------
  function setupBlogPage() {
    const blogFilterBtns = document.querySelectorAll('.blog-filter-btn');
    const blogCards = document.querySelectorAll('.blog-card');

    if (blogFilterBtns.length > 0 && blogCards.length > 0) {
      blogFilterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          blogFilterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const category = btn.dataset.category;
          blogCards.forEach(card => {
            if (category === 'all' || card.dataset.category === category) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          });
        });
      });
    }

    // Article Read Buttons
    document.querySelectorAll('.btn-read-article').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.blog-card') || btn.closest('.featured-article-card');
        if (!card) return;

        const title = card.querySelector('h2, h3')?.textContent.trim() || 'Italian Culinary Guide';
        const img = card.querySelector('img')?.getAttribute('src') || 'images/article_emulsion.jpg';
        const excerpt = card.querySelector('p')?.textContent.trim() || '';

        openArticleModal({ title, img, excerpt });
      });
    });
  }

  function openArticleModal(data) {
    let modal = document.querySelector('.article-reader-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.className = 'modal-overlay article-reader-modal';
      modal.innerHTML = `
        <div class="article-modal" style="position:relative;">
          <button type="button" class="modal-close-btn">&times;</button>
          <span class="eyebrow"><i class="fa-solid fa-book-open"></i> Pastificio Artigianale Journal</span>
          <h1 class="art-title">${data.title}</h1>
          <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
            By <strong>Maestro Giancarlo</strong> &bull; Sfoglino dell'Emilia &bull; 6 min read
          </div>
          <img src="${data.img}" alt="${data.title}" class="article-modal-img">
          <div class="article-modal-text">
            <p><strong>${data.excerpt}</strong></p>
            <p>The alchemy of handmade pasta relies on three simple elements: stone-milled semolina, pristine spring water or farm-fresh egg yolks, and time. When kneading dough by hand on untreated beechwood, micro-fissures develop on the surface of the sheet (sfoglia). These minute textures become the anchor points where sauce binds irrevocably to each strand.</p>
            <h3>1. The Golden Rule of Salted Boiling Water</h3>
            <p>Water should taste clean like the Mediterranean Sea — approximately 10 grams of coarse Sicilian sea salt per liter of water. Adding salt too early slows down the boil; instead, dissolve it right as the water reaches a vigorous rolling boil before dropping the fresh noodles.</p>
            <h3>2. The Science of Bronze Die Extrusion</h3>
            <p>Unlike industrial teflon dies that produce glossy, slippery pasta surfaces, traditional bronze dies shear the dough under immense pressure. This leaves an artisanal matte, flour-dusted chalkiness on the outer crust of penne, rigatoni, and bucatini that captures emulsions effortlessly.</p>
            <h3>3. The Magic of "Acqua di Cottura"</h3>
            <p>Never discard your pasta cooking water! The starch released during the 3-minute boil acts as a natural emulsifying liaison. By tossing al dente pasta into a pan with warm olive oil, butter, or pan juices and ladling in 60ml of hot starchy water, you create a velvety, restaurant-grade emulsion without needing heavy cream.</p>
          </div>
          <div style="margin-top:2.5rem; padding-top:1.5rem; border-top:1px solid var(--beige-border); display:flex; justify-content:space-between; align-items:center;">
            <div style="font-size:0.85rem; color:var(--text-muted);">Share this guide with fellow home pasta makers:</div>
            <div style="display:flex; gap:0.5rem;">
              <button class="btn btn-outline-navy btn-sm" onclick="showToast('Article link copied to clipboard!','info')"><i class="fa-solid fa-share-nodes"></i> Share</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      modal.querySelector('.modal-close-btn').addEventListener('click', closeModals);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModals();
      });
    } else {
      modal.querySelector('.art-title').textContent = data.title;
      modal.querySelector('.article-modal-img').src = data.img;
      modal.querySelector('.article-modal-text p strong').textContent = data.excerpt;
    }

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  // -------------------------------------------------------------
  // 10. NEWSLETTER VALIDATION (FOOTER & BODY)
  // -------------------------------------------------------------
  function setupNewsletterForms() {
    const forms = document.querySelectorAll('.newsletter-form, #footerNewsletterForm, #homeNewsletterForm, .nss-form');
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = form.querySelector('input[type="email"], .newsletter-input');
        if (!emailInput || !emailInput.value.trim()) {
          showToast('Please enter your email address.', 'error');
          return;
        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailInput.value.trim())) {
          showToast('Please enter a valid email address.', 'error');
          return;
        }

        showToast('Benvenuto! You are now subscribed to our weekly Italian Deli letter.', 'success');
        form.reset();
      });
    });
  }

  // -------------------------------------------------------------
  // INITIALIZE ON DOM READY
  // -------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', () => {
    initThemeAndRTL();
    updateCartUI();
    setupDrawers();
    setupHeader();
    setupProductsPage();
    setupCateringPage();
    setupContactPage();
    setupBlogPage();
    setupNewsletterForms();
  });

})();

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
