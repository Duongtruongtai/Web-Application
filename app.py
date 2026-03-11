from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bài tập Cloud của tôi</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { color: #333; }
            .section { margin-bottom: 20px; padding: 15px; border-left: 5px solid #007bff; background-color: #f8f9fa; }
        </style>
    </head>
    <body>
        <h1>Xin chào! Đây là bài tập Cloud của tôi.</h1>
        <div class="section">
            <h2>1. Thông tin sinh viên</h2>
            <p><strong>Họ và tên:</strong> [Tên của bạn]</p>
            <p><strong>Mã số sinh viên:</strong> [MSSV của bạn]</p>
            <p><strong>Lớp:</strong> [Lớp của bạn]</p>
        </div>
        <div class="section">
            <h2>2. Mô tả bài làm</h2>
            <p>Web App này được triển khai trên <strong>Render.com</strong> (Nền tảng PaaS miễn phí).</p>
            <p>Ứng dụng sử dụng <strong>Python Flask</strong> cho phần backend và HTML/CSS cho frontend.</p>
        </div>
        <div class="section">
            <h2>3. Kiến trúc hệ thống</h2>
            <p>User -> Internet -> Render Platform (Public URL) -> Ứng dụng Flask (Gunicorn Web Server) -> Nội dung HTML</p>
        </div>
        <div class="section">
            <h2>4. Bảo mật</h2>
            <p>Nền tảng Render tự động cấu hình firewall, chỉ cho phép truy cập qua cổng 80 (HTTP) và 443 (HTTPS).</p>
            <p>HTTPS được bật tự động và miễn phí.</p>
            <p>Truy cập server chỉ qua tài khoản Render và Git.</p>
        </div>
        <p><em>Ngày hoàn thành: [Ngày hiện tại]</em></p>
    </body>
    </html>
    """