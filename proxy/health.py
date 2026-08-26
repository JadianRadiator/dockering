from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass # Keeps logs clean from health check flooding

if __name__ == "__main__":
    print("Health check server running on port 10000...")
    HTTPServer(('0.0.0.0', 10000), HealthHandler).serve_forever()
