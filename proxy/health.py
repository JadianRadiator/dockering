import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass # Suppress log flooding from Render health probes

def run_health_server():
    print("Health check web server active on port 10000...")
    HTTPServer(('0.0.0.0', 10000), HealthHandler).serve_forever()

if __name__ == "__main__":
    # 1. Fire up Render's health check server in a background thread
    threading.Thread(target=run_health_server, daemon=True).start()
    
    # 2. Fire up Gost in the foreground process
    print("Launching Gost proxy engine on port 8080...")
    subprocess.run(["/bin/gost", "-L=http://JadianRadiator:MaJiCkA@:8080"])
