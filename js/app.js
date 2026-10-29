/**
 * Marimo Shop - Main Application Script
 * ショッピングサイトのフロントエンド処理全般を制御
 */

document.addEventListener('DOMContentLoaded', () => {
  // ==========================================
  // 状態管理 (State)
  // ==========================================
  let currentCategory = 'all';
  let searchQuery = '';
  let currentSort = 'recommended';
  let cart = [];

  // 定数
  const FREE_SHIPPING_THRESHOLD = 5000; // 送料無料ライン（円）
  const STANDARD_SHIPPING_FEE = 550;    // 通常送料（円）
  const CART_STORAGE_KEY = 'marimo_shop_cart_v1';

  // ==========================================
  // DOM要素の取得
  // ==========================================
  const productsGrid = document.getElementById('productsGrid');
  const productsCountEl = document.getElementById('productsCount');
  const categoryTabs = document.querySelectorAll('.tab-btn');
  const sortSelect = document.getElementById('sortSelect');
  const searchInput = document.getElementById('searchInput');
  const mobileSearchInput = document.getElementById('mobileSearchInput');

  // カート関連要素
  const cartBtn = document.getElementById('cartBtn');
  const mobileCartBtn = document.getElementById('mobileCartBtn');
  const cartBadge = document.getElementById('cartBadge');
  const mobileCartBadge = document.getElementById('mobileCartBadge');
  const cartDrawer = document.getElementById('cartDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const cartItemsList = document.getElementById('cartItemsList');
  const cartEmptyView = document.getElementById('cartEmptyView');
  const cartSubtotalEl = document.getElementById('cartSubtotal');
  const cartShippingEl = document.getElementById('cartShipping');
  const cartTotalEl = document.getElementById('cartTotal');
  const cartClearBtn = document.getElementById('cartClearBtn');
  const checkoutBtn = document.getElementById('checkoutBtn');
  const shippingAlertText = document.getElementById('shippingAlertText');
  const shippingBarFill = document.getElementById('shippingBarFill');

  // 購入手続きモーダル要素
  const checkoutModal = document.getElementById('checkoutModal');
  const checkoutCloseBtn = document.getElementById('checkoutCloseBtn');
  const checkoutForm = document.getElementById('checkoutForm');
  const summaryItemsContainer = document.getElementById('summaryItemsContainer');
  const checkoutSubtotalEl = document.getElementById('checkoutSubtotal');
  const checkoutShippingEl = document.getElementById('checkoutShipping');
  const checkoutTotalEl = document.getElementById('checkoutTotal');

  // 注文完了モーダル要素
  const completeModal = document.getElementById('completeModal');
  const completeOrderNumber = document.getElementById('completeOrderNumber');
  const completeOrderDate = document.getElementById('completeOrderDate');
  const completeOrderName = document.getElementById('completeOrderName');
  const completeOrderAddress = document.getElementById('completeOrderAddress');
  const completeOrderPayment = document.getElementById('completeOrderPayment');
  const completeOrderTotal = document.getElementById('completeOrderTotal');
  const backToShopBtn = document.getElementById('backToShopBtn');

  // トースト要素
  const toastContainer = document.getElementById('toastContainer');

  // ==========================================
  // 初期化 (Initialization)
  // ==========================================
  loadCartFromStorage();
  renderProducts();
  updateCartUI();
  setupEventListeners();

  // ==========================================
  // 商品表示・フィルタリング・ソート
  // ==========================================
  function getFilteredProducts() {
    let items = [...PRODUCTS_DATA];

    // カテゴリフィルター
    if (currentCategory !== 'all') {
      items = items.filter(item => 
        item.category === currentCategory || item.group === currentCategory
      );
    }

    // 検索ワードフィルター
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase().trim();
      items = items.filter(item =>
        item.name.toLowerCase().includes(q) ||
        item.description.toLowerCase().includes(q) ||
        item.categoryName.toLowerCase().includes(q)
      );
    }

    // 並び替えソート
    if (currentSort === 'price-low') {
      items.sort((a, b) => a.price - b.price);
    } else if (currentSort === 'price-high') {
      items.sort((a, b) => b.price - a.price);
    } else if (currentSort === 'rating') {
      items.sort((a, b) => b.rating - a.rating);
    } else {
      // recommended (ID順)
      items.sort((a, b) => a.id - b.id);
    }

    return items;
  }

  function renderProducts() {
    const products = getFilteredProducts();
    productsCountEl.innerHTML = `該当商品: <strong>${products.length}</strong> 件`;

    if (products.length === 0) {
      productsGrid.innerHTML = `
        <div class="no-results">
          <div class="no-results-icon">🍃</div>
          <div class="no-results-text">条件に一致する商品が見つかりませんでした</div>
          <div class="no-results-sub">カテゴリーを変えるか、別の検索キーワードをお試しください。</div>
        </div>
      `;
      return;
    }

    productsGrid.innerHTML = products.map(product => `
      <article class="product-card" data-id="${product.id}">
        <div class="product-image-wrap">
          <img src="${product.image}" alt="${escapeHtml(product.name)}" class="product-image" loading="lazy">
          ${product.badge ? `<span class="product-badge">${escapeHtml(product.badge)}</span>` : ''}
        </div>
        <div class="product-info">
          <span class="product-category-tag">${escapeHtml(product.categoryName)}</span>
          <h3 class="product-title">${escapeHtml(product.name)}</h3>
          <div class="product-rating">
            <span>★</span>
            <strong>${product.rating.toFixed(1)}</strong>
            <span class="rating-count">(${product.reviewsCount})</span>
          </div>
          <p class="product-desc">${escapeHtml(product.description)}</p>
          <div class="product-footer">
            <div class="product-price-box">
              <span class="product-price">¥${product.price.toLocaleString()}</span>
              <span class="product-tax">税込</span>
            </div>
            <button class="add-to-cart-btn" data-id="${product.id}" title="カートに追加">
              <span>🛒</span> カートに入れる
            </button>
          </div>
        </div>
      </article>
    `).join('');
  }

  // ==========================================
  // カート管理ロジック
  // ==========================================
  function loadCartFromStorage() {
    try {
      const saved = localStorage.getItem(CART_STORAGE_KEY);
      if (saved) {
        cart = JSON.parse(saved);
      }
    } catch (e) {
      console.warn('カートの読み込みに失敗しました:', e);
      cart = [];
    }
  }

  function saveCartToStorage() {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
    } catch (e) {
      console.warn('カートの保存に失敗しました:', e);
    }
  }

  function addToCart(productId) {
    const product = PRODUCTS_DATA.find(p => p.id === productId);
    if (!product) return;

    const existingItem = cart.find(item => item.id === productId);
    if (existingItem) {
      existingItem.quantity += 1;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
        categoryName: product.categoryName,
        quantity: 1
      });
    }

    saveCartToStorage();
    updateCartUI();
    showToast(`「${product.name}」をカートに追加しました`);
  }

  function updateItemQuantity(productId, delta) {
    const item = cart.find(i => i.id === productId);
    if (!item) return;

    item.quantity += delta;
    if (item.quantity <= 0) {
      removeFromCart(productId);
      return;
    }

    saveCartToStorage();
    updateCartUI();
  }

  function removeFromCart(productId) {
    const item = cart.find(i => i.id === productId);
    if (!item) return;

    const name = item.name;
    cart = cart.filter(i => i.id !== productId);
    saveCartToStorage();
    updateCartUI();
    showToast(`「${name}」をカートから削除しました`);
  }

  function clearCart() {
    if (cart.length === 0) return;
    if (confirm('カート内の商品をすべて削除しますか？')) {
      cart = [];
      saveCartToStorage();
      updateCartUI();
      showToast('カートを空にしました');
    }
  }

  function calculateCartTotals() {
    const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const shipping = subtotal >= FREE_SHIPPING_THRESHOLD || subtotal === 0 ? 0 : STANDARD_SHIPPING_FEE;
    const total = subtotal + shipping;

    return { totalCount, subtotal, shipping, total };
  }

  function updateCartUI() {
    const { totalCount, subtotal, shipping, total } = calculateCartTotals();

    // バッジ更新
    cartBadge.textContent = totalCount;
    if (mobileCartBadge) mobileCartBadge.textContent = totalCount;

    // 送料無料アラート更新
    if (subtotal === 0) {
      shippingAlertText.innerHTML = `あと <strong>¥${FREE_SHIPPING_THRESHOLD.toLocaleString()}</strong> で<strong>送料無料</strong>になります`;
      shippingBarFill.style.width = '0%';
    } else if (subtotal >= FREE_SHIPPING_THRESHOLD) {
      shippingAlertText.innerHTML = `🎉 <strong>送料無料</strong>でお届けします！`;
      shippingBarFill.style.width = '100%';
    } else {
      const diff = FREE_SHIPPING_THRESHOLD - subtotal;
      const percent = Math.min(100, Math.round((subtotal / FREE_SHIPPING_THRESHOLD) * 100));
      shippingAlertText.innerHTML = `あと <strong>¥${diff.toLocaleString()}</strong> で<strong>送料無料</strong>になります`;
      shippingBarFill.style.width = `${percent}%`;
    }

    // カート内アイテム一覧表示
    if (cart.length === 0) {
      cartItemsList.style.display = 'none';
      cartEmptyView.style.display = 'flex';
      checkoutBtn.disabled = true;
      checkoutBtn.style.opacity = '0.5';
      checkoutBtn.style.cursor = 'not-allowed';
    } else {
      cartItemsList.style.display = 'flex';
      cartEmptyView.style.display = 'none';
      checkoutBtn.disabled = false;
      checkoutBtn.style.opacity = '1';
      checkoutBtn.style.cursor = 'pointer';

      cartItemsList.innerHTML = cart.map(item => `
        <div class="cart-item" data-id="${item.id}">
          <img src="${item.image}" alt="${escapeHtml(item.name)}" class="cart-item-img">
          <div class="cart-item-details">
            <h4 class="cart-item-title">${escapeHtml(item.name)}</h4>
            <div class="cart-item-price">¥${(item.price * item.quantity).toLocaleString()} <span style="font-size:0.75rem;color:var(--color-text-muted);">(¥${item.price.toLocaleString()}/点)</span></div>
            <div class="cart-item-controls">
              <div class="quantity-control">
                <button class="qty-btn" data-action="decrease" data-id="${item.id}" title="数量を減らす">−</button>
                <input type="text" class="qty-input" value="${item.quantity}" readonly>
                <button class="qty-btn" data-action="increase" data-id="${item.id}" title="数量を増やす">＋</button>
              </div>
              <button class="item-remove-btn" data-id="${item.id}">
                🗑️ 削除
              </button>
            </div>
          </div>
        </div>
      `).join('');
    }

    // 金額表示の更新
    cartSubtotalEl.textContent = `¥${subtotal.toLocaleString()}`;
    cartShippingEl.textContent = shipping === 0 ? (subtotal > 0 ? '無料' : '¥0') : `¥${shipping.toLocaleString()}`;
    cartTotalEl.textContent = `¥${total.toLocaleString()}`;
  }

  // ==========================================
  // モーダル & ドロワー開閉
  // ==========================================
  function openCartDrawer() {
    cartDrawer.classList.add('active');
    drawerBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCartDrawer() {
    cartDrawer.classList.remove('active');
    drawerBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  function openCheckoutModal() {
    if (cart.length === 0) {
      alert('カートに商品が入っていません。');
      return;
    }
    closeCartDrawer();

    // 注文サマリーの構築
    const { subtotal, shipping, total } = calculateCartTotals();
    summaryItemsContainer.innerHTML = cart.map(item => `
      <div class="summary-item-row">
        <span class="summary-item-name">${escapeHtml(item.name)} × ${item.quantity}</span>
        <span>¥${(item.price * item.quantity).toLocaleString()}</span>
      </div>
    `).join('');

    checkoutSubtotalEl.textContent = `¥${subtotal.toLocaleString()}`;
    checkoutShippingEl.textContent = shipping === 0 ? '無料' : `¥${shipping.toLocaleString()}`;
    checkoutTotalEl.textContent = `¥${total.toLocaleString()}`;

    checkoutModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCheckoutModal() {
    checkoutModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function openCompleteModal(orderData) {
    closeCheckoutModal();

    completeOrderNumber.textContent = orderData.orderNumber;
    completeOrderDate.textContent = orderData.date;
    completeOrderName.textContent = `${orderData.name} 様`;
    completeOrderAddress.textContent = `〒${orderData.zip} ${orderData.address}`;
    completeOrderPayment.textContent = orderData.paymentMethod;
    completeOrderTotal.textContent = `¥${orderData.total.toLocaleString()} (税込・送料込)`;

    completeModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeCompleteModal() {
    completeModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // ==========================================
  // 注文処理
  // ==========================================
  function handleCheckoutSubmit(e) {
    e.preventDefault();

    if (cart.length === 0) {
      alert('カートが空です。');
      return;
    }

    const formData = new FormData(checkoutForm);
    const name = formData.get('userName')?.trim();
    const zip = formData.get('userZip')?.trim();
    const address = formData.get('userAddress')?.trim();
    const phone = formData.get('userPhone')?.trim();
    const email = formData.get('userEmail')?.trim();
    const payment = formData.get('paymentMethod');

    // 簡易バリデーション
    if (!name || !zip || !address || !phone || !email) {
      alert('必須項目をすべてご入力ください。');
      return;
    }

    const { total } = calculateCartTotals();

    // 注文番号の生成 (例: MRM-20261029-4821)
    const today = new Date();
    const dateStr = today.toISOString().slice(0, 10).replace(/-/g, '');
    const randomNum = Math.floor(1000 + Math.random() * 9000);
    const orderNumber = `MRM-${dateStr}-${randomNum}`;

    const paymentMap = {
      'credit': 'クレジットカード決済',
      'convenience': 'コンビニ決済',
      'cod': '代金引換',
      'bank': '銀行振込'
    };

    const orderData = {
      orderNumber,
      date: today.toLocaleString('ja-JP', { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }),
      name,
      zip,
      address,
      paymentMethod: paymentMap[payment] || 'クレジットカード決済',
      total
    };

    // フォームリセット & カートクリア
    checkoutForm.reset();
    cart = [];
    saveCartToStorage();
    updateCartUI();

    // 完了画面表示
    openCompleteModal(orderData);
  }

  // ==========================================
  // トースト通知
  // ==========================================
  let toastTimer = null;
  function showToast(message) {
    // 既存トーストをクリア
    toastContainer.innerHTML = '';
    if (toastTimer) clearTimeout(toastTimer);

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span class="toast-icon">✓</span> <span>${escapeHtml(message)}</span>`;
    toastContainer.appendChild(toast);

    // アニメーション表示
    requestAnimationFrame(() => {
      toast.classList.add('show');
    });

    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, 2800);
  }

  // ==========================================
  // ユーティリティ
  // ==========================================
  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // ==========================================
  // イベントリスナー設定
  // ==========================================
  function setupEventListeners() {
    // カテゴリータブ切り替え
    categoryTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        categoryTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        currentCategory = tab.dataset.category;
        renderProducts();
      });
    });

    // ソート切り替え
    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      renderProducts();
    });

    // 検索入力 (PC & モバイル同期)
    const handleSearch = (val) => {
      searchQuery = val;
      if (searchInput) searchInput.value = val;
      if (mobileSearchInput) mobileSearchInput.value = val;
      renderProducts();
    };

    if (searchInput) {
      searchInput.addEventListener('input', (e) => handleSearch(e.target.value));
    }
    if (mobileSearchInput) {
      mobileSearchInput.addEventListener('input', (e) => handleSearch(e.target.value));
    }

    // 商品一覧での「カートに入れる」クリック
    productsGrid.addEventListener('click', (e) => {
      const btn = e.target.closest('.add-to-cart-btn');
      if (btn) {
        const id = parseInt(btn.dataset.id, 10);
        addToCart(id);
      }
    });

    // カートドロワー内での数量変更・削除クリック
    cartItemsList.addEventListener('click', (e) => {
      const qtyBtn = e.target.closest('.qty-btn');
      if (qtyBtn) {
        const id = parseInt(qtyBtn.dataset.id, 10);
        const action = qtyBtn.dataset.action;
        updateItemQuantity(id, action === 'increase' ? 1 : -1);
        return;
      }

      const removeBtn = e.target.closest('.item-remove-btn');
      if (removeBtn) {
        const id = parseInt(removeBtn.dataset.id, 10);
        removeFromCart(id);
        return;
      }
    });

    // カートを空にするボタン
    cartClearBtn.addEventListener('click', clearCart);

    // カートドロワーの開閉
    cartBtn.addEventListener('click', openCartDrawer);
    if (mobileCartBtn) mobileCartBtn.addEventListener('click', openCartDrawer);
    drawerCloseBtn.addEventListener('click', closeCartDrawer);
    drawerBackdrop.addEventListener('click', closeCartDrawer);

    // 購入手続きへ進む
    checkoutBtn.addEventListener('click', openCheckoutModal);
    checkoutCloseBtn.addEventListener('click', closeCheckoutModal);

    // 注文フォーム送信
    checkoutForm.addEventListener('submit', handleCheckoutSubmit);

    // 注文完了画面の「買い物を続ける」
    backToShopBtn.addEventListener('click', closeCompleteModal);

    // ESCキーでモーダルを閉じる
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeCartDrawer();
        closeCheckoutModal();
        closeCompleteModal();
      }
    });
  }
});
