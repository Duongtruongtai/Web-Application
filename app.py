from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bài tập Cloud - Dương Trường Tài</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            
            .container {
                max-width: 900px;
                margin: 30px auto;
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                overflow: hidden;
                animation: slideIn 0.5s ease;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(-30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                text-align: center;
            }
            
            .header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            
            .header .subtitle {
                font-size: 1.2em;
                opacity: 0.95;
            }
            
            .content {
                padding: 40px;
            }
            
            .section {
                background: #f8f9fa;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 25px;
                border-left: 5px solid #667eea;
                transition: transform 0.3s ease;
            }
            
            .section:hover {
                transform: translateX(10px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            
            .section h2 {
                color: #333;
                margin-bottom: 15px;
                font-size: 1.5em;
                display: flex;
                align-items: center;
            }
            
            .section h2:before {
                content: "•";
                color: #667eea;
                font-size: 1.5em;
                margin-right: 10px;
            }
            
            .info-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 15px;
                margin-top: 15px;
            }
            
            .info-item {
                background: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            }
            
            .info-item strong {
                color: #667eea;
                display: block;
                margin-bottom: 5px;
                font-size: 0.9em;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .info-item p {
                color: #555;
                font-size: 1.1em;
            }
            
            .badge {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                margin-right: 10px;
                margin-bottom: 10px;
            }
            
            .architecture {
                background: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-family: monospace;
                font-size: 1.1em;
                color: #555;
                border: 2px dashed #667eea;
            }
            
            .footer {
                text-align: center;
                padding: 20px;
                background: #f1f3f5;
                color: #666;
                font-size: 0.9em;
            }
            
            .footer a {
                color: #667eea;
                text-decoration: none;
            }
            
            .footer a:hover {
                text-decoration: underline;
            }
            
            @media (max-width: 768px) {
                .header h1 {
                    font-size: 1.8em;
                }
                
                .content {
                    padding: 20px;
                }
                
                .section {
                    padding: 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📚 BÀI TẬP CLOUD COMPUTING</h1>
                <p class="subtitle">Triển khai Web App trên Render Platform</p>
            </div>
            
            <div class="content">
                <!-- Thông tin sinh viên -->
                <div class="section">
                    <h2>👨‍🎓 Thông tin sinh viên</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <strong>Họ và tên</strong>
                            <p>Dương Trường Tài</p>
                        </div>
                        <div class="info-item">
                            <strong>Mã số sinh viên</strong>
                            <p>123001011</p>
                        </div>
                        <div class="info-item">
                            <strong>Lớp</strong>
                            <p>23AI111</p>
                        </div>
                    </div>
                </div>
                
                <!-- Công nghệ sử dụng -->
                <div class="section">
                    <h2>🛠️ Công nghệ sử dụng</h2>
                    <div>
                        <span class="badge">Python Flask</span>
                        <span class="badge">HTML5/CSS3</span>
                        <span class="badge">Gunicorn</span>
                        <span class="badge">Render (PaaS)</span>
                        <span class="badge">Hostinger DNS</span>
                        <span class="badge">Let's Encrypt SSL</span>
                    </div>
                </div>
                
                <!-- Kiến trúc hệ thống -->
                <div class="section">
                    <h2>🏗️ Kiến trúc hệ thống</h2>
                    <div class="architecture">
                        👤 User → 🌐 Internet → 📡 DNS (Hostinger) → 🚀 Render Platform → 🐍 Flask App → 📄 HTML Response
                    </div>
                    <p style="margin-top: 15px; color: #666;">
                        <strong>Chi tiết:</strong> Khi user truy cập <strong>toy9999.com</strong>, request được DNS trỏ về IP của Render. 
                        Render nhận request, chuyển đến web server Gunicorn, server gọi Flask app xử lý và trả về nội dung HTML.
                    </p>
                </div>
                
                <!-- Bảo mật -->
                <div class="section">
                    <h2>🔒 Bảo mật</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <strong>HTTPS/SSL</strong>
                            <p>✅ Let's Encrypt (tự động gia hạn)</p>
                        </div>
                        <div class="info-item">
                            <strong>Firewall</strong>
                            <p>✅ Render quản lý - chỉ mở port 80, 443</p>
                        </div>
                        <div class="info-item">
                            <strong>DDoS Protection</strong>
                            <p>✅ Render cung cấp cơ bản</p>
                        </div>
                        <div class="info-item">
                            <strong>DNS Security</strong>
                            <p>✅ DNSSEC (Hostinger)</p>
                        </div>
                    </div>
                </div>
                
                <!-- Thông tin triển khai -->
                <div class="section">
                    <h2>📦 Thông tin triển khai</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <strong>Nền tảng</strong>
                            <p>Render.com (Free Tier)</p>
                        </div>
                        <div class="info-item">
                            <strong>Domain</strong>
                            <p>toy9999.com (Hostinger)</p>
                        </div>
                        <div class="info-item">
                            <strong>Ngày deploy</strong>
                            <p>11/03/2026</p>
                        </div>
                        <div class="info-item">
                            <strong>Trạng thái</strong>
                            <p>✅ Hoạt động</p>
                        </div>
                    </div>
                </div>
                
                <!-- Link kiểm tra -->
                <div class="section">
                    <h2>🔗 Link truy cập</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <strong>Domain chính</strong>
                            <p><a href="https://toy9999.com" target="_blank">https://toy9999.com</a> ✅</p>
                        </div>
                        <div class="info-item">
                            <strong>Subdomain www</strong>
                            <p><a href="https://www.toy9999.com" target="_blank">https://www.toy9999.com</a> ✅</p>
                        </div>
                        <div class="info-item">
                            <strong>Render URL</strong>
                            <p><a href="https://web-application-7vkr.onrender.com" target="_blank">web-application-7vkr.onrender.com</a></p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>📝 Bài tập Cloud Computing - Đại học LẠC HỒNG UNIVERSITY</p>
                <p>📧 Liên hệ: duongtruongtai.lhu@gmail.com | ⏰ Hoàn thành: 11/03/2026</p>
                <p>✨ <a href="#" onclick="alert('Cảm ơn giảng viên đã xem bài của em ạ!')">Demo trực tiếp</a> ✨</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)