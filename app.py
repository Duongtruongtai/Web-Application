from flask import Flask, render_template_string, request, jsonify
import json

app = Flask(__name__)

# Dữ liệu sản phẩm mẫu
products = [
    {
        "id": 1,
        "name": "LEGO Technic Porsche 911",
        "price": 2490000,
        "old_price": 2990000,
        "image": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=400",
        "category": "lego",
        "rating": 4.8,
        "sold": 156,
        "description": "Mô hình lắp ráp Porsche 911 chi tiết, 1580 chi tiết"
    },
    {
        "id": 2,
        "name": "Gấu bông Capybara 1m",
        "price": 450000,
        "old_price": 650000,
        "image": "https://images.unsplash.com/photo-1584992236006-bb63b3b161b5?w=400",
        "category": "stuffed",
        "rating": 4.9,
        "sold": 328,
        "description": "Gấu bông capybara siêu mềm mại, cao 1m"
    },
    {
        "id": 3,
        "name": "Hot Wheels Monster Truck",
        "price": 189000,
        "old_price": 249000,
        "image": "https://images.unsplash.com/photo-1594787318286-3d835c1d207f?w=400",
        "category": "cars",
        "rating": 4.7,
        "sold": 412,
        "description": "Xe điều khiển monster truck siêu khủng"
    },
    {
        "id": 4,
        "name": "Rubik 3x3 Speed Cube",
        "price": 299000,
        "old_price": 399000,
        "image": "https://images.unsplash.com/photo-1591991564021-0662a8573199?w=400",
        "category": "puzzle",
        "rating": 4.6,
        "sold": 289,
        "description": "Rubik tốc độ cao, trơn tru, không kẹt"
    },
    {
        "id": 5,
        "name": "Máy bay điều khiển 2 kênh",
        "price": 890000,
        "old_price": 1290000,
        "image": "https://images.unsplash.com/photo-1578302758063-0ef3e048ca89?w=400",
        "category": "rc",
        "rating": 4.5,
        "sold": 67,
        "description": "Máy bay điều khiển 2 kênh, bay ổn định"
    },
    {
        "id": 6,
        "name": "Bộ đồ chơi bác sĩ 32 món",
        "price": 350000,
        "old_price": 499000,
        "image": "https://images.unsplash.com/photo-1558863654-f5c11a5c369b?w=400",
        "category": "roleplay",
        "rating": 4.8,
        "sold": 203,
        "description": "Bộ đồ chơi bác sĩ đa năng, an toàn cho bé"
    },
    {
        "id": 7,
        "name": "Búp bê Baby Annabell",
        "price": 1290000,
        "old_price": 1590000,
        "image": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=400",
        "category": "dolls",
        "rating": 4.9,
        "sold": 92,
        "description": "Búp bê biết khóc, biết ăn, cao 43cm"
    },
    {
        "id": 8,
        "name": "Bộ xếp hình gỗ 100 chi tiết",
        "price": 299000,
        "old_price": 399000,
        "image": "https://images.unsplash.com/photo-1618365429382-9e8671b31006?w=400",
        "category": "wooden",
        "rating": 4.7,
        "sold": 178,
        "description": "Đồ chơi xếp hình gỗ, an toàn, giáo dục"
    }
]

# Giỏ hàng tạm thời (trong thực tế nên dùng session hoặc database)
cart = []

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, products=products, cart_count=len(cart))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return render_template_string(PRODUCT_DETAIL_TEMPLATE, product=product, cart_count=len(cart))
    return "Product not found", 404

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart_item = {
            "id": product_id,
            "name": product["name"],
            "price": product["price"],
            "image": product["image"],
            "quantity": quantity
        }
        cart.append(cart_item)
        return jsonify({"success": True, "cart_count": len(cart)})
    return jsonify({"success": False}), 400

@app.route('/cart')
def view_cart():
    total = sum(item["price"] * item["quantity"] for item in cart)
    return render_template_string(CART_TEMPLATE, cart=cart, total=total, cart_count=len(cart))

# HTML Template chính
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToyStore - Shop đồ chơi trẻ em</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background: #f5f5f5;
        }
        
        /* Header */
        .header {
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 28px;
            font-weight: bold;
            text-decoration: none;
            color: white;
        }
        
        .logo span {
            color: #ffe66d;
        }
        
        .search-box {
            flex: 0 1 400px;
            display: flex;
            gap: 10px;
        }
        
        .search-box input {
            flex: 1;
            padding: 10px 15px;
            border: none;
            border-radius: 25px;
            outline: none;
            font-size: 14px;
        }
        
        .search-box button {
            background: #ffe66d;
            border: none;
            border-radius: 25px;
            padding: 10px 25px;
            cursor: pointer;
            font-weight: bold;
            color: #333;
        }
        
        .header-icons {
            display: flex;
            gap: 25px;
        }
        
        .header-icons a {
            color: white;
            text-decoration: none;
            position: relative;
        }
        
        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ffe66d;
            color: #333;
            font-size: 12px;
            padding: 2px 6px;
            border-radius: 50%;
        }
        
        /* Banner */
        .banner {
            background: linear-gradient(135deg, #4158D0, #C850C0);
            color: white;
            padding: 60px 20px;
            text-align: center;
            margin-bottom: 40px;
        }
        
        .banner h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .banner p {
            font-size: 20px;
            margin-bottom: 30px;
        }
        
        .banner button {
            background: #ffe66d;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
            cursor: pointer;
            transition: transform 0.3s;
        }
        
        .banner button:hover {
            transform: scale(1.05);
        }
        
        /* Categories */
        .categories {
            max-width: 1200px;
            margin: 0 auto 40px;
            padding: 0 20px;
        }
        
        .category-list {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .category-item {
            background: white;
            padding: 10px 25px;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .category-item:hover {
            background: #ff6b6b;
            color: white;
            transform: translateY(-2px);
        }
        
        .category-item.active {
            background: #ff6b6b;
            color: white;
        }
        
        /* Products */
        .products-section {
            max-width: 1200px;
            margin: 0 auto 60px;
            padding: 0 20px;
        }
        
        .section-title {
            font-size: 32px;
            color: #333;
            margin-bottom: 30px;
            text-align: center;
        }
        
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }
        
        .product-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s;
            position: relative;
        }
        
        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        
        .product-badge {
            position: absolute;
            top: 15px;
            left: 15px;
            background: #ff6b6b;
            color: white;
            padding: 5px 15px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: bold;
            z-index: 1;
        }
        
        .product-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
            transition: transform 0.3s;
        }
        
        .product-card:hover .product-image {
            transform: scale(1.05);
        }
        
        .product-info {
            padding: 20px;
        }
        
        .product-name {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            height: 50px;
            overflow: hidden;
        }
        
        .product-rating {
            color: #ffc107;
            margin-bottom: 10px;
        }
        
        .product-rating span {
            color: #666;
            margin-left: 5px;
        }
        
        .product-price {
            font-size: 24px;
            font-weight: bold;
            color: #ff6b6b;
            margin-bottom: 5px;
        }
        
        .product-old-price {
            font-size: 16px;
            color: #999;
            text-decoration: line-through;
            margin-left: 10px;
        }
        
        .product-sold {
            color: #666;
            font-size: 14px;
            margin-bottom: 15px;
        }
        
        .add-to-cart {
            width: 100%;
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.3s;
        }
        
        .add-to-cart:hover {
            opacity: 0.9;
        }
        
        /* Footer */
        .footer {
            background: #333;
            color: white;
            padding: 60px 20px 20px;
        }
        
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
        }
        
        .footer-section h3 {
            margin-bottom: 20px;
            color: #ffe66d;
        }
        
        .footer-section p {
            margin-bottom: 10px;
            color: #ccc;
        }
        
        .footer-bottom {
            text-align: center;
            padding-top: 40px;
            color: #ccc;
            border-top: 1px solid #555;
            margin-top: 40px;
        }
        
        /* Toast notification */
        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #333;
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            animation: slideIn 0.3s ease;
            z-index: 1001;
        }
        
        @keyframes slideIn {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <a href="/" class="logo">Toy<span>Store</span></a>
            
            <div class="search-box">
                <input type="text" id="search" placeholder="Tìm kiếm đồ chơi...">
                <button onclick="searchProducts()">Tìm</button>
            </div>
            
            <div class="header-icons">
                <a href="/">🏠 Trang chủ</a>
                <a href="/cart">🛒 Giỏ hàng <span class="cart-count">{{ cart_count }}</span></a>
                <a href="#">👤 Tài khoản</a>
            </div>
        </div>
    </div>
    
    <div class="banner">
        <h1>🎁 SIÊU SALE - GIẢM ĐẾN 50%</h1>
        <p>Mua sắm đồ chơi cho bé yêu với giá ưu đãi nhất</p>
        <button onclick="document.querySelector('.products-section').scrollIntoView({behavior: 'smooth'})">
            Mua sắm ngay
        </button>
    </div>
    
    <div class="categories">
        <div class="category-list">
            <span class="category-item active">Tất cả</span>
            <span class="category-item">LEGO</span>
            <span class="category-item">Gấu bông</span>
            <span class="category-item">Xe điều khiển</span>
            <span class="category-item">Đồ chơi giáo dục</span>
            <span class="category-item">Búp bê</span>
        </div>
    </div>
    
    <div class="products-section">
        <h2 class="section-title">🔥 Sản phẩm nổi bật</h2>
        <div class="product-grid">
            {% for product in products %}
            <div class="product-card">
                <div class="product-badge">-{{ ((product.old_price - product.price) / product.old_price * 100) | int }}%</div>
                <a href="/product/{{ product.id }}" style="text-decoration: none; color: inherit;">
                    <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image">
                </a>
                <div class="product-info">
                    <div class="product-name">{{ product.name }}</div>
                    <div class="product-rating">
                        {% for i in range(5) %}
                            {% if i < product.rating|int %}
                                ★
                            {% elif product.rating - i > 0.5 %}
                                ★
                            {% else %}
                                ☆
                            {% endif %}
                        {% endfor %}
                        <span>({{ product.rating }})</span>
                    </div>
                    <div>
                        <span class="product-price">{{ "{:,.0f}".format(product.price) }}₫</span>
                        <span class="product-old-price">{{ "{:,.0f}".format(product.old_price) }}₫</span>
                    </div>
                    <div class="product-sold">Đã bán {{ product.sold }}</div>
                    <button class="add-to-cart" onclick="addToCart({{ product.id }})">
                        Thêm vào giỏ
                    </button>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    
    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>🎪 Về chúng tôi</h3>
                <p>🏢 Đại học LẠC HỒNG UNIVERSITY</p>
                <p>👨‍🎓 Sinh viên: Dương Trường Tài</p>
                <p>📧 Email: duongtruongtai.lhu@gmail.com</p>
                <p>📚 MSSV: 123001011 - Lớp: 23AI111</p>
            </div>
            <div class="footer-section">
                <h3>📞 Hỗ trợ khách hàng</h3>
                <p>Hotline: 1900 1234</p>
                <p>Email: support@toystore.com</p>
                <p>Thời gian: 8h - 22h hàng ngày</p>
            </div>
            <div class="footer-section">
                <h3>📝 Bài tập Cloud</h3>
                <p>✅ Triển khai trên Render.com</p>
                <p>✅ Domain: toy9999.com</p>
                <p>✅ SSL: Let's Encrypt</p>
                <p>✅ Flask + HTML/CSS</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 - Bài tập Cloud Computing - Dương Trường Tài</p>
            <p>📅 Hoàn thành: 11/03/2026</p>
        </div>
    </div>
    
    <script>
        function addToCart(productId) {
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_id: productId,
                    quantity: 1
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Cập nhật số lượng giỏ hàng trên header
                    document.querySelector('.cart-count').textContent = data.cart_count;
                    
                    // Hiển thị thông báo
                    showToast('✅ Đã thêm sản phẩm vào giỏ hàng!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('❌ Có lỗi xảy ra!');
            });
        }
        
        function showToast(message) {
            const toast = document.createElement('div');
            toast.className = 'toast';
            toast.textContent = message;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.remove();
            }, 3000);
        }
        
        function searchProducts() {
            const searchTerm = document.getElementById('search').value;
            if (searchTerm) {
                alert('Chức năng tìm kiếm đang phát triển. Hiện tại bạn có thể xem tất cả sản phẩm!');
            }
        }
        
        // Filter products by category (đơn giản)
        document.querySelectorAll('.category-item').forEach(item => {
            item.addEventListener('click', function() {
                document.querySelectorAll('.category-item').forEach(c => c.classList.remove('active'));
                this.classList.add('active');
                
                const category = this.textContent;
                if (category === 'Tất cả') {
                    document.querySelectorAll('.product-card').forEach(card => {
                        card.style.display = 'block';
                    });
                } else {
                    alert('Chức năng lọc đang phát triển. Hiện tại bạn có thể xem tất cả sản phẩm!');
                }
            });
        });
    </script>
</body>
</html>
"""

# Template chi tiết sản phẩm
PRODUCT_DETAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} - ToyStore</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }
        
        .header {
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 28px;
            font-weight: bold;
            text-decoration: none;
            color: white;
        }
        
        .logo span {
            color: #ffe66d;
        }
        
        .header-icons a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            position: relative;
        }
        
        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ffe66d;
            color: #333;
            font-size: 12px;
            padding: 2px 6px;
            border-radius: 50%;
        }
        
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }
        
        .product-detail {
            background: white;
            border-radius: 20px;
            padding: 40px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        
        .product-images {
            position: relative;
        }
        
        .main-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 15px;
        }
        
        .product-badge {
            position: absolute;
            top: 20px;
            left: 20px;
            background: #ff6b6b;
            color: white;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: bold;
        }
        
        .product-info h1 {
            font-size: 32px;
            color: #333;
            margin-bottom: 20px;
        }
        
        .rating {
            color: #ffc107;
            font-size: 18px;
            margin-bottom: 20px;
        }
        
        .price-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        .current-price {
            font-size: 36px;
            font-weight: bold;
            color: #ff6b6b;
        }
        
        .old-price {
            font-size: 20px;
            color: #999;
            text-decoration: line-through;
            margin-left: 15px;
        }
        
        .discount {
            background: #ff6b6b;
            color: white;
            padding: 5px 15px;
            border-radius: 25px;
            margin-left: 15px;
        }
        
        .description {
            margin-bottom: 30px;
            line-height: 1.8;
            color: #666;
        }
        
        .quantity {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
        }
        
        .quantity button {
            width: 40px;
            height: 40px;
            background: #f1f3f5;
            border: none;
            border-radius: 8px;
            font-size: 20px;
            cursor: pointer;
        }
        
        .quantity input {
            width: 80px;
            height: 40px;
            text-align: center;
            border: 1px solid #ddd;
            border-radius: 8px;
        }
        
        .add-to-cart {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.3s;
        }
        
        .add-to-cart:hover {
            opacity: 0.9;
        }
        
        .back-link {
            display: inline-block;
            margin-top: 20px;
            color: #666;
            text-decoration: none;
        }
        
        .footer {
            background: #333;
            color: white;
            padding: 40px 20px 20px;
            margin-top: 60px;
        }
        
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <a href="/" class="logo">Toy<span>Store</span></a>
            <div class="header-icons">
                <a href="/">🏠 Trang chủ</a>
                <a href="/cart">🛒 Giỏ hàng <span class="cart-count">{{ cart_count }}</span></a>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="product-detail">
            <div class="product-images">
                <img src="{{ product.image }}" alt="{{ product.name }}" class="main-image">
                <div class="product-badge">
                    -{{ ((product.old_price - product.price) / product.old_price * 100) | int }}%
                </div>
            </div>
            
            <div class="product-info">
                <h1>{{ product.name }}</h1>
                
                <div class="rating">
                    {% for i in range(5) %}
                        {% if i < product.rating|int %}
                            ★
                        {% elif product.rating - i > 0.5 %}
                            ★
                        {% else %}
                            ☆
                        {% endif %}
                    {% endfor %}
                    <span style="color: #666; margin-left: 10px;">({{ product.rating }} sao - {{ product.sold }} đã bán)</span>
                </div>
                
                <div class="price-box">
                    <span class="current-price">{{ "{:,.0f}".format(product.price) }}₫</span>
                    <span class="old-price">{{ "{:,.0f}".format(product.old_price) }}₫</span>
                    <span class="discount">Tiết kiệm {{ "{:,.0f}".format(product.old_price - product.price) }}₫</span>
                </div>
                
                <div class="description">
                    <h3>Mô tả sản phẩm:</h3>
                    <p>{{ product.description }}</p>
                    <p style="margin-top: 15px;">✅ Thương hiệu: ToyStore</p>
                    <p>✅ Chất liệu: An toàn cho trẻ em</p>
                    <p>✅ Bảo hành: 12 tháng</p>
                </div>
                
                <div class="quantity">
                    <span style="font-weight: bold;">Số lượng:</span>
                    <button onclick="decrement()">-</button>
                    <input type="number" id="quantity" value="1" min="1" max="99">
                    <button onclick="increment()">+</button>
                </div>
                
                <button class="add-to-cart" onclick="addToCart({{ product.id }})">
                    🛒 Thêm vào giỏ hàng
                </button>
                
                <a href="/" class="back-link">← Quay lại trang chủ</a>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <div class="footer-content">
            <p>&copy; 2026 - Bài tập Cloud Computing - Dương Trường Tài (MSSV: 123001011)</p>
            <p>Triển khai trên Render - Domain: toy9999.com</p>
        </div>
    </div>
    
    <script>
        function increment() {
            let input = document.getElementById('quantity');
            input.value = parseInt(input.value) + 1;
        }
        
        function decrement() {
            let input = document.getElementById('quantity');
            if (parseInt(input.value) > 1) {
                input.value = parseInt(input.value) - 1;
            }
        }
        
        function addToCart(productId) {
            const quantity = document.getElementById('quantity').value;
            
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_id: productId,
                    quantity: parseInt(quantity)
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Cập nhật số lượng giỏ hàng
                    document.querySelector('.cart-count').textContent = data.cart_count;
                    
                    // Hiển thị thông báo
                    alert('✅ Đã thêm ' + quantity + ' sản phẩm vào giỏ hàng!');
                    
                    // Hỏi có muốn xem giỏ hàng không
                    if (confirm('Sản phẩm đã được thêm vào giỏ hàng. Bạn muốn xem giỏ hàng ngay?')) {
                        window.location.href = '/cart';
                    }
                }
            });
        }
    </script>
</body>
</html>
"""

# Template giỏ hàng
CART_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giỏ hàng - ToyStore</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }
        
        .header {
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 28px;
            font-weight: bold;
            text-decoration: none;
            color: white;
        }
        
        .logo span {
            color: #ffe66d;
        }
        
        .header-icons a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            position: relative;
        }
        
        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ffe66d;
            color: #333;
            font-size: 12px;
            padding: 2px 6px;
            border-radius: 50%;
        }
        
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }
        
        h1 {
            color: #333;
            margin-bottom: 30px;
        }
        
        .cart-empty {
            text-align: center;
            padding: 60px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .cart-empty p {
            font-size: 18px;
            color: #666;
            margin-bottom: 20px;
        }
        
        .cart-empty a {
            display: inline-block;
            padding: 12px 30px;
            background: #ff6b6b;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }
        
        .cart-items {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .cart-item {
            display: grid;
            grid-template-columns: 100px 1fr auto;
            gap: 20px;
            padding: 20px;
            border-bottom: 1px solid #eee;
        }
        
        .cart-item img {
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 10px;
        }
        
        .item-info h3 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .item-price {
            font-size: 18px;
            font-weight: bold;
            color: #ff6b6b;
        }
        
        .cart-summary {
            background: #f8f9fa;
            padding: 30px;
            margin-top: 20px;
            border-radius: 15px;
            text-align: right;
        }
        
        .total {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }
        
        .total span {
            color: #ff6b6b;
            font-size: 32px;
            margin-left: 15px;
        }
        
        .checkout-btn {
            padding: 15px 40px;
            background: linear-gradient(135deg, #ff6b6b, #ff8e8e);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }
        
        .continue-shopping {
            display: inline-block;
            margin-top: 20px;
            color: #666;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-content">
            <a href="/" class="logo">Toy<span>Store</span></a>
            <div class="header-icons">
                <a href="/">🏠 Trang chủ</a>
                <a href="/cart">🛒 Giỏ hàng <span class="cart-count">{{ cart_count }}</span></a>
            </div>
        </div>
    </div>
    
    <div class="container">
        <h1>🛒 Giỏ hàng của bạn</h1>
        
        {% if cart %}
        <div class="cart-items">
            {% for item in cart %}
            <div class="cart-item">
                <img src="{{ item.image }}" alt="{{ item.name }}">
                <div class="item-info">
                    <h3>{{ item.name }}</h3>
                    <p>Số lượng: {{ item.quantity }}</p>
                    <p class="item-price">{{ "{:,.0f}".format(item.price * item.quantity) }}₫</p>
                </div>
                <div>
                    <button onclick="alert('Chức năng xóa đang phát triển')" style="background: none; border: none; color: #ff6b6b; cursor: pointer;">✖</button>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="cart-summary">
            <div class="total">
                Tổng tiền: <span>{{ "{:,.0f}".format(total) }}₫</span>
            </div>
            <button class="checkout-btn" onclick="alert('Cảm ơn bạn đã mua hàng! (Demo - chức năng thanh toán đang phát triển)')">
                Tiến hành thanh toán
            </button>
            <br>
            <a href="/" class="continue-shopping">← Tiếp tục mua sắm</a>
        </div>
        {% else %}
        <div class="cart-empty">
            <p>🛒 Giỏ hàng của bạn đang trống</p>
            <a href="/">Mua sắm ngay</a>
        </div>
        {% endif %}
    </div>
    
    <div class="footer">
        <div class="footer-content">
            <p>&copy; 2026 - Bài tập Cloud Computing - Dương Trường Tài (MSSV: 123001011)</p>
        </div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)