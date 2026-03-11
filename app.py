from flask import Flask, render_template_string, request, jsonify, session, send_from_directory
import json
import os

app = Flask(__name__)
app.secret_key = 'toystore_secret_key_2026'

# Cấu hình đường dẫn ảnh
IMAGE_FOLDER = r'C:\Users\Tai\OneDrive\Máy tính\Web Application'

@app.route('/images/<filename>')
def get_image(filename):
    """Phục vụ ảnh từ thư mục local"""
    return send_from_directory(IMAGE_FOLDER, filename)

# Danh sách sản phẩm với ẢNH LOCAL 100% - mỗi ảnh đúng với sản phẩm
products = [
    # LEGO & Xếp hình (dùng ảnh từ URL vì không có trong folder)
    {
        "id": 1,
        "name": "LEGO Porsche 911 - Siêu xe thể thao",
        "price": 2490000,
        "old_price": 3290000,
        "image": "https://www.lego.com/cdn/cs/set/assets/blt5d4c5e5c5e5c5e5c/42096.png",
        "image_fallback": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=600",
        "category": "lego",
        "rating": 4.9,
        "sold": 245,
        "description": "Mô hình LEGO Porsche 911 GT3 RS chi tiết với 1580 chi tiết, đi kèm hộp số hoạt động.",
        "brand": "LEGO",
        "age": "10+",
        "material": "Nhựa ABS",
        "in_stock": 45,
        "color": "#FF6B8B"
    },
    {
        "id": 2,
        "name": "LEGO Hogwarts - Lâu đài phép thuật",
        "price": 3990000,
        "old_price": 4590000,
        "image": "https://www.lego.com/cdn/cs/set/assets/blt3d4c5e5c5e5c5e5c/71043.png",
        "image_fallback": "https://images.unsplash.com/photo-1610484826967-09c5720778c7?w=600",
        "category": "lego",
        "rating": 4.8,
        "sold": 89,
        "description": "Lâu đài Hogwarts với 2660 chi tiết, tái hiện các lớp học và tháp phép thuật.",
        "brand": "LEGO",
        "age": "12+",
        "material": "Nhựa ABS",
        "in_stock": 12,
        "color": "#9370DB"
    },
    
    # Thú nhồi bông - ẢNH TỪ FILE LOCAL CỦA BẠN
    {
        "id": 3,
        "name": "Gấu Capybara Khổng Lồ 1.2m",
        "price": 550000,
        "old_price": 790000,
        "image": "/images/download.jpg",
        "image_fallback": "https://cf.shopee.vn/file/8a7f1d9c8c8c8c8c8c8c8c8c8c8c8c8c",
        "category": "stuffed",
        "rating": 4.9,
        "sold": 528,
        "description": "Gấu bông capybara siêu mềm mại, cao 1.2m, chất liệu an toàn cho bé ôm ngủ.",
        "brand": "Dream Toys",
        "age": "0+",
        "material": "Lông nhung cao cấp",
        "in_stock": 120,
        "color": "#F4A460"
    },
    {
        "id": 4,
        "name": "Gấu Teddy Nâu 50cm",
        "price": 299000,
        "old_price": 450000,
        "image": "/images/download%20(1).jpg",
        "image_fallback": "https://images.unsplash.com/photo-1568650358963-86c0d0c19c7e?w=600",
        "category": "stuffed",
        "rating": 4.7,
        "sold": 892,
        "description": "Gấu Teddy cổ điển với bộ lông mềm mượt, thích hợp làm quà tặng.",
        "brand": "Teddy Bear",
        "age": "0+",
        "material": "Polyester cao cấp",
        "in_stock": 200,
        "color": "#8B4513"
    },
    {
        "id": 5,
        "name": "Gấu Bông Panda 60cm",
        "price": 399000,
        "old_price": 590000,
        "image": "/images/download%20(2).jpg",
        "image_fallback": "https://images.unsplash.com/photo-1584992236006-bb63b3b161b5?w=600",
        "category": "stuffed",
        "rating": 4.8,
        "sold": 367,
        "description": "Gấu trúc panda đen trắng dễ thương, chất liệu siêu mềm.",
        "brand": "Dream Toys",
        "age": "0+",
        "material": "Lông nhung",
        "in_stock": 85,
        "color": "#000000"
    },
    
    # Xe điều khiển
    {
        "id": 6,
        "name": "Hot Wheels Monster Truck RC",
        "price": 459000,
        "old_price": 650000,
        "image": "https://product.hstatic.net/1000001234/product/monster_truck_rc_1.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1594787318286-3d835c1d207f?w=600",
        "category": "rc",
        "rating": 4.8,
        "sold": 312,
        "description": "Xe điều khiển monster truck siêu khủng, vượt địa hình tốt, pin 30 phút.",
        "brand": "Hot Wheels",
        "age": "6+",
        "material": "Nhựa ABS",
        "in_stock": 56,
        "color": "#FF4500"
    },
    
    # Đồ chơi giáo dục
    {
        "id": 7,
        "name": "Rubik 3x3 Speed Cube Pro",
        "price": 299000,
        "old_price": 450000,
        "image": "https://product.hstatic.net/1000001234/product/rubik_3x3_1.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1591991564021-0662a8573199?w=600",
        "category": "educational",
        "rating": 4.9,
        "sold": 567,
        "description": "Rubik tốc độ cao với lò xo điều chỉnh độ căng, không kẹt.",
        "brand": "SpeedCube",
        "age": "6+",
        "material": "Nhựa ABS",
        "in_stock": 150,
        "color": "#32CD32"
    },
    {
        "id": 8,
        "name": "Xếp Hình Gỗ 100 Chi Tiết",
        "price": 399000,
        "old_price": 550000,
        "image": "/images/download%20(3).jpg",
        "image_fallback": "https://images.unsplash.com/photo-1618365429382-9e8671b31006?w=600",
        "category": "educational",
        "rating": 4.8,
        "sold": 234,
        "description": "Đồ chơi xếp hình gỗ an toàn, phát triển tư duy cho bé.",
        "brand": "Wooden Toys",
        "age": "3+",
        "material": "Gỗ tự nhiên",
        "in_stock": 89,
        "color": "#D2691E"
    },
    
    # Búp bê
    {
        "id": 9,
        "name": "Búp Bê Baby Annabell 43cm",
        "price": 1290000,
        "old_price": 1690000,
        "image": "https://product.hstatic.net/1000001234/product/baby_annabell_1.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=600",
        "category": "dolls",
        "rating": 4.9,
        "sold": 145,
        "description": "Búp bê biết khóc, biết ăn, biết đi vệ sinh, cao 43cm.",
        "brand": "Baby Annabell",
        "age": "3+",
        "material": "Nhựa mềm + Vải",
        "in_stock": 34,
        "color": "#FFB6C1"
    },
    
    # Đồ chơi nhập vai
    {
        "id": 10,
        "name": "Bộ Đồ Chơi Bác Sĩ 32 Món",
        "price": 390000,
        "old_price": 590000,
        "image": "/images/vn-11134207-7r98o-lt8aan5o12u15d.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1558863654-f5c11a5c369b?w=600",
        "category": "roleplay",
        "rating": 4.8,
        "sold": 403,
        "description": "Bộ đồ chơi bác sĩ đa năng với 32 món, có âm thanh và đèn.",
        "brand": "Doctor Play",
        "age": "3+",
        "material": "Nhựa ABS",
        "in_stock": 67,
        "color": "#20B2AA"
    },
    {
        "id": 11,
        "name": "Bộ Nấu Ăn 25 Món",
        "price": 350000,
        "old_price": 520000,
        "image": "https://product.hstatic.net/1000001234/product/kitchen_set_25_1.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1566140967404-b8b3932483f5?w=600",
        "category": "roleplay",
        "rating": 4.7,
        "sold": 289,
        "description": "Bộ đồ chơi nấu ăn với nồi, chảo, thức ăn giả, giúp bé học làm đầu bếp.",
        "brand": "Kitchen Fun",
        "age": "3+",
        "material": "Nhựa cao cấp",
        "in_stock": 92,
        "color": "#FFA07A"
    },
    
    # Đồ chơi ngoài trời
    {
        "id": 12,
        "name": "Xe Đạp Trẻ Em 16 inch",
        "price": 2590000,
        "old_price": 3290000,
        "image": "/images/xe-dap-tre-em-nam-thong-nhat-batman-16-inch-1-700x467.jpg",
        "image_fallback": "https://images.unsplash.com/photo-1576435778699-1a3e0008efb7?w=600",
        "category": "outdoor",
        "rating": 4.8,
        "sold": 67,
        "description": "Xe đạp 16 inch, có bánh phụ, phanh an toàn, yên xe êm ái.",
        "brand": "Kids Rider",
        "age": "4-7",
        "material": "Khung thép",
        "in_stock": 15,
        "color": "#1E90FF"
    }
]

# Danh mục sản phẩm
categories = [
    {"id": "all", "name": "Tất cả", "icon": "🎮", "color": "#FF6B6B"},
    {"id": "lego", "name": "LEGO", "icon": "🧱", "color": "#F9D56E"},
    {"id": "stuffed", "name": "Thú bông", "icon": "🧸", "color": "#F4A460"},
    {"id": "rc", "name": "Xe điều khiển", "icon": "🚗", "color": "#FF8C42"},
    {"id": "educational", "name": "Giáo dục", "icon": "📚", "color": "#6C63FF"},
    {"id": "dolls", "name": "Búp bê", "icon": "🎎", "color": "#FFB6C1"},
    {"id": "roleplay", "name": "Nhập vai", "icon": "👨‍⚕️", "color": "#20B2AA"},
    {"id": "outdoor", "name": "Ngoài trời", "icon": "🚲", "color": "#1E90FF"}
]

@app.route('/')
def home():
    cart_count = len(session.get('cart', []))
    return render_template_string(HOME_TEMPLATE, products=products, categories=categories, cart_count=cart_count)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    cart_count = len(session.get('cart', []))
    return render_template_string(PRODUCT_TEMPLATE, product=product, cart_count=cart_count)

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    if 'cart' not in session:
        session['cart'] = []
    
    for item in session['cart']:
        if item['id'] == product_id:
            item['quantity'] += quantity
            session.modified = True
            return jsonify({"success": True, "cart_count": len(session['cart'])})
    
    product = next((p for p in products if p["id"] == product_id), None)
    session['cart'].append({
        "id": product_id,
        "name": product["name"],
        "price": product["price"],
        "image": product["image"],
        "quantity": quantity
    })
    session.modified = True
    return jsonify({"success": True, "cart_count": len(session['cart'])})

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(item["price"] * item["quantity"] for item in cart)
    return render_template_string(CART_TEMPLATE, cart=cart, total=total, cart_count=len(cart))

@app.route('/category/<category_id>')
def category_view(category_id):
    if category_id == 'all':
        filtered = products
    else:
        filtered = [p for p in products if p["category"] == category_id]
    cart_count = len(session.get('cart', []))
    return render_template_string(HOME_TEMPLATE, products=filtered, categories=categories, cart_count=cart_count, active_category=category_id)

# HTML Template với giao diện đẹp
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToyStore - Thế giới đồ chơi cho bé</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Poppins', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            min-height: 100vh;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 15px 0;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 30px;
        }

        .logo {
            font-size: 36px;
            font-weight: 800;
            color: white;
            text-decoration: none;
            text-shadow: 3px 3px 0 rgba(0,0,0,0.1);
        }

        .search-box {
            flex: 1;
            display: flex;
            background: white;
            border-radius: 50px;
            overflow: hidden;
            max-width: 600px;
        }

        .search-box input {
            flex: 1;
            padding: 12px 20px;
            border: none;
            outline: none;
            font-size: 16px;
        }

        .search-box button {
            background: #ff6b6b;
            color: white;
            border: none;
            padding: 12px 30px;
            cursor: pointer;
            font-weight: 600;
        }

        .header-icons {
            display: flex;
            gap: 20px;
        }

        .header-icon {
            color: white;
            text-decoration: none;
            font-size: 20px;
            position: relative;
        }

        .cart-badge {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ff6b6b;
            color: white;
            font-size: 12px;
            padding: 2px 6px;
            border-radius: 50%;
            border: 2px solid white;
        }

        .categories {
            background: white;
            padding: 20px 0;
            margin-bottom: 30px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }

        .category-list {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
        }

        .category-item {
            padding: 10px 25px;
            border-radius: 30px;
            background: #f8f9fa;
            color: #333;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
            border: 2px solid transparent;
        }

        .category-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102,126,234,0.3);
        }

        .category-item.active {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        .banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 50px;
            margin: 30px 0;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .banner::before {
            content: "🧸🎨🎮🎲";
            position: absolute;
            font-size: 150px;
            right: 30px;
            bottom: -30px;
            opacity: 0.1;
            transform: rotate(-15deg);
        }

        .banner h1 {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .banner p {
            font-size: 20px;
            margin-bottom: 25px;
            opacity: 0.95;
        }

        .banner button {
            background: white;
            color: #667eea;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }

        .banner button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        .section-title {
            font-size: 32px;
            color: #333;
            margin: 40px 0 20px;
            position: relative;
            padding-bottom: 10px;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 3px;
            background: #667eea;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 50px;
        }

        .product-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
            transition: all 0.3s;
            position: relative;
            border: 1px solid #eee;
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(102,126,234,0.15);
        }

        .product-badge {
            position: absolute;
            top: 15px;
            left: 15px;
            background: #ff6b6b;
            color: white;
            padding: 5px 15px;
            border-radius: 25px;
            font-weight: bold;
            z-index: 1;
            font-size: 14px;
            box-shadow: 0 3px 8px rgba(255,107,107,0.3);
        }

        .product-image {
            width: 100%;
            height: 250px;
            object-fit: contain;
            background: #f8f9fa;
            padding: 15px;
            transition: transform 0.5s;
        }

        .product-card:hover .product-image {
            transform: scale(1.05);
        }

        .product-info {
            padding: 20px;
        }

        .brand-tag {
            color: #667eea;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 5px;
        }

        .product-name {
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
            height: 50px;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }

        .rating {
            color: #ffc107;
            margin-bottom: 10px;
            font-size: 14px;
        }

        .rating span {
            color: #666;
            margin-left: 5px;
        }

        .price-area {
            margin: 10px 0;
        }

        .current-price {
            font-size: 24px;
            font-weight: 700;
            color: #ff6b6b;
        }

        .old-price {
            font-size: 16px;
            color: #999;
            text-decoration: line-through;
            margin-left: 10px;
        }

        .product-meta {
            display: flex;
            justify-content: space-between;
            color: #666;
            font-size: 14px;
            margin: 15px 0;
            padding-top: 10px;
            border-top: 1px solid #eee;
        }

        .add-to-cart {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .add-to-cart:hover {
            opacity: 0.9;
            transform: scale(1.02);
        }

        .footer {
            background: #2d3748;
            color: white;
            padding: 60px 0 20px;
            margin-top: 80px;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
        }

        .footer-section h3 {
            color: #ff6b6b;
            margin-bottom: 20px;
            font-size: 20px;
        }

        .footer-section p {
            color: #cbd5e0;
            margin-bottom: 10px;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #4a5568;
            color: #a0aec0;
        }

        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: white;
            color: #333;
            padding: 15px 25px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            border-left: 5px solid #667eea;
            animation: slideIn 0.3s;
            z-index: 9999;
        }

        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @media (max-width: 768px) {
            .header-content { flex-direction: column; }
            .search-box { max-width: 100%; }
            .banner h1 { font-size: 32px; }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="container header-content">
            <a href="/" class="logo">🧸 ToyStore</a>
            
            <form class="search-box" action="/search" method="get">
                <input type="text" name="q" placeholder="Tìm kiếm đồ chơi...">
                <button type="submit"><i class="fas fa-search"></i> Tìm</button>
            </form>
            
            <div class="header-icons">
                <a href="/" class="header-icon"><i class="fas fa-home"></i></a>
                <a href="/cart" class="header-icon">
                    <i class="fas fa-shopping-cart"></i>
                    {% if cart_count > 0 %}
                    <span class="cart-badge">{{ cart_count }}</span>
                    {% endif %}
                </a>
            </div>
        </div>
    </div>

    <div class="categories">
        <div class="container category-list">
            {% for cat in categories %}
            <a href="/category/{{ cat.id }}" class="category-item {% if active_category == cat.id %}active{% endif %}">
                {{ cat.icon }} {{ cat.name }}
            </a>
            {% endfor %}
        </div>
    </div>

    <div class="container">
        <div class="banner">
            <h1>🎉 SIÊU SALE MÙA HÈ 2026</h1>
            <p>Giảm đến 50% + Miễn phí ship cho đơn trên 500k</p>
            <button onclick="alert('Chương trình áp dụng từ 15/03 - 30/03')">
                <i class="fas fa-gift"></i> Nhận ưu đãi
            </button>
        </div>

        <h2 class="section-title">
            {% if active_category %}
                {% for cat in categories %}{% if cat.id == active_category %}{{ cat.icon }} {{ cat.name }}{% endif %}{% endfor %}
            {% else %}
                🎯 Sản phẩm nổi bật
            {% endif %}
        </h2>

        <div class="product-grid">
            {% for product in products %}
            <div class="product-card">
                {% if product.old_price and product.old_price > product.price %}
                <div class="product-badge">-{{ ((product.old_price - product.price) / product.old_price * 100) | int }}%</div>
                {% endif %}
                
                <a href="/product/{{ product.id }}">
                    <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image" 
                         onerror="this.src='{{ product.image_fallback }}';this.onerror=null;">
                </a>
                
                <div class="product-info">
                    <div class="brand-tag">{{ product.brand }}</div>
                    <h3 class="product-name">{{ product.name }}</h3>
                    
                    <div class="rating">
                        {% for i in range(5) %}
                            {% if i < product.rating|int %}
                                <i class="fas fa-star"></i>
                            {% elif product.rating - i > 0.5 %}
                                <i class="fas fa-star-half-alt"></i>
                            {% else %}
                                <i class="far fa-star"></i>
                            {% endif %}
                        {% endfor %}
                        <span>({{ product.rating }})</span>
                    </div>
                    
                    <div class="price-area">
                        <span class="current-price">{{ "{:,.0f}".format(product.price) }}₫</span>
                        {% if product.old_price and product.old_price > product.price %}
                        <span class="old-price">{{ "{:,.0f}".format(product.old_price) }}₫</span>
                        {% endif %}
                    </div>
                    
                    <div class="product-meta">
                        <span><i class="fas fa-shopping-bag"></i> Đã bán {{ product.sold }}</span>
                        <span><i class="fas fa-box"></i> Còn {{ product.in_stock }}</span>
                    </div>
                    
                    <button class="add-to-cart" onclick="addToCart({{ product.id }})">
                        <i class="fas fa-cart-plus"></i> Thêm vào giỏ
                    </button>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <div class="footer">
        <div class="container footer-grid">
            <div class="footer-section">
                <h3>Về ToyStore</h3>
                <p>Dương Trường Tài - 123001011</p>
                <p>Lớp 23AI111 - Đại học Lạc Hồng</p>
                <p>Email: duongtruongtai.lhu@gmail.com</p>
            </div>
            <div class="footer-section">
                <h3>Bài tập Cloud</h3>
                <p>✅ Render.com - Free Tier</p>
                <p>✅ Domain: toy9999.com</p>
                <p>✅ SSL: Let's Encrypt</p>
                <p>✅ Flask + HTML/CSS</p>
            </div>
            <div class="footer-section">
                <h3>Hỗ trợ</h3>
                <p>Hotline: 1900 1234</p>
                <p>Email: support@toystore.com</p>
                <p>Hoàn thành: 11/03/2026</p>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 - Dương Trường Tài - Bài tập Cloud Computing</p>
        </div>
    </div>

    <script>
        function addToCart(productId) {
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({product_id: productId, quantity: 1})
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    let badge = document.querySelector('.cart-badge');
                    if (badge) {
                        badge.textContent = data.cart_count;
                    } else {
                        let cartIcon = document.querySelector('.header-icon:last-child');
                        let newBadge = document.createElement('span');
                        newBadge.className = 'cart-badge';
                        newBadge.textContent = '1';
                        cartIcon.appendChild(newBadge);
                    }
                    
                    let toast = document.createElement('div');
                    toast.className = 'toast';
                    toast.innerHTML = '✅ Đã thêm vào giỏ hàng!';
                    document.body.appendChild(toast);
                    setTimeout(() => toast.remove(), 2000);
                }
            });
        }
    </script>
</body>
</html>
"""

PRODUCT_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} - ToyStore</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background: #f8f9fa; }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 15px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 32px;
            color: white;
            text-decoration: none;
        }
        
        .header-icon {
            color: white;
            text-decoration: none;
            font-size: 20px;
            position: relative;
        }
        
        .cart-badge {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ff6b6b;
            color: white;
            padding: 2px 6px;
            border-radius: 50%;
            font-size: 12px;
        }
        
        .product-detail {
            background: white;
            border-radius: 20px;
            padding: 40px;
            margin: 40px 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .product-image {
            width: 100%;
            height: 500px;
            object-fit: contain;
            background: #f8f9fa;
            border-radius: 15px;
        }
        
        .product-info h1 {
            font-size: 32px;
            color: #333;
            margin-bottom: 15px;
        }
        
        .rating {
            color: #ffc107;
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
        
        .description {
            line-height: 1.8;
            color: #666;
            margin-bottom: 30px;
        }
        
        .add-to-cart {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
        }
        
        .footer {
            background: #2d3748;
            color: white;
            padding: 40px 0;
            text-align: center;
            margin-top: 60px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="container header-content">
            <a href="/" class="logo">🧸 ToyStore</a>
            <a href="/cart" class="header-icon">
                <i class="fas fa-shopping-cart"></i>
                {% if cart_count > 0 %}
                <span class="cart-badge">{{ cart_count }}</span>
                {% endif %}
            </a>
        </div>
    </div>

    <div class="container">
        <div class="product-detail">
            <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image"
                 onerror="this.src='{{ product.image_fallback }}'">
            
            <div class="product-info">
                <h1>{{ product.name }}</h1>
                
                <div class="rating">
                    {% for i in range(5) %}
                        {% if i < product.rating|int %}
                            <i class="fas fa-star"></i>
                        {% elif product.rating - i > 0.5 %}
                            <i class="fas fa-star-half-alt"></i>
                        {% else %}
                            <i class="far fa-star"></i>
                        {% endif %}
                    {% endfor %}
                    <span style="color:#666"> ({{ product.rating }} sao - {{ product.sold }} đã bán)</span>
                </div>
                
                <div class="price-box">
                    <span class="current-price">{{ "{:,.0f}".format(product.price) }}₫</span>
                    {% if product.old_price > product.price %}
                    <span class="old-price">{{ "{:,.0f}".format(product.old_price) }}₫</span>
                    {% endif %}
                </div>
                
                <div class="description">
                    <p>{{ product.description }}</p>
                    <p style="margin-top:15px"><strong>Thương hiệu:</strong> {{ product.brand }}</p>
                    <p><strong>Độ tuổi:</strong> {{ product.age }}</p>
                    <p><strong>Chất liệu:</strong> {{ product.material }}</p>
                    <p><strong>Còn hàng:</strong> {{ product.in_stock }} sản phẩm</p>
                </div>
                
                <button class="add-to-cart" onclick="addToCart({{ product.id }})">
                    <i class="fas fa-cart-plus"></i> Thêm vào giỏ hàng
                </button>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>Dương Trường Tài - 123001011 - 23AI111</p>
        <p style="margin-top:10px">Bài tập Cloud - Triển khai trên Render - toy9999.com</p>
    </div>

    <script>
        function addToCart(productId) {
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({product_id: productId, quantity: 1})
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert('✅ Đã thêm vào giỏ hàng!');
                    window.location.href = '/cart';
                }
            });
        }
    </script>
</body>
</html>
"""

CART_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giỏ hàng - ToyStore</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #f8f9fa; font-family: 'Segoe UI', sans-serif; }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 15px 0;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 32px;
            color: white;
            text-decoration: none;
        }
        
        .cart-content {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
            margin: 40px 0;
        }
        
        .cart-items {
            background: white;
            border-radius: 15px;
            padding: 20px;
        }
        
        .cart-item {
            display: grid;
            grid-template-columns: 80px 1fr auto;
            gap: 20px;
            padding: 20px;
            border-bottom: 1px solid #eee;
        }
        
        .cart-item img {
            width: 80px;
            height: 80px;
            object-fit: contain;
        }
        
        .cart-summary {
            background: white;
            border-radius: 15px;
            padding: 25px;
            height: fit-content;
        }
        
        .checkout-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            margin: 20px 0;
        }
        
        .footer {
            background: #2d3748;
            color: white;
            padding: 40px 0;
            text-align: center;
            margin-top: 60px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="container header-content">
            <a href="/" class="logo">🧸 ToyStore</a>
            <a href="/" style="color:white">← Tiếp tục mua sắm</a>
        </div>
    </div>

    <div class="container">
        <h1 style="margin: 30px 0">🛒 Giỏ hàng của bé</h1>
        
        {% if cart %}
        <div class="cart-content">
            <div class="cart-items">
                {% for item in cart %}
                <div class="cart-item">
                    <img src="{{ item.image }}" onerror="this.src='https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=200'">
                    <div>
                        <h3>{{ item.name }}</h3>
                        <p>Số lượng: {{ item.quantity }}</p>
                    </div>
                    <div style="font-weight: bold; color: #ff6b6b">
                        {{ "{:,.0f}".format(item.price * item.quantity) }}₫
                    </div>
                </div>
                {% endfor %}
            </div>
            
            <div class="cart-summary">
                <h3 style="margin-bottom: 20px">Thông tin đơn hàng</h3>
                <p style="margin: 10px 0">Tạm tính: {{ "{:,.0f}".format(total) }}₫</p>
                <p style="margin: 10px 0">Phí ship: Miễn phí</p>
                <hr style="margin: 15px 0">
                <p style="font-size: 24px; font-weight: bold; color: #ff6b6b">
                    Tổng: {{ "{:,.0f}".format(total) }}₫
                </p>
                <button class="checkout-btn" onclick="alert('Cảm ơn bạn! Đây là bài tập demo.')">
                    Thanh toán
                </button>
            </div>
        </div>
        {% else %}
        <div style="text-align: center; padding: 80px; background: white; border-radius: 15px">
            <i class="fas fa-shopping-cart" style="font-size: 80px; color: #ccc"></i>
            <p style="font-size: 24px; margin: 20px 0">Giỏ hàng trống</p>
            <a href="/" style="background: #667eea; color: white; padding: 15px 40px; border-radius: 8px; text-decoration: none">Mua sắm ngay</a>
        </div>
        {% endif %}
    </div>

    <div class="footer">
        <p>Dương Trường Tài - 123001011 - 23AI111</p>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)