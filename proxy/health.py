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
        pass 

def run_health_server():
    print("Health check web server active on port 10000...")
    HTTPServer(('0.0.0.0', 10000), HealthHandler).serve_forever()

if __name__ == "__main__":
    # Start Render's health monitoring responder thread
    threading.Thread(target=run_health_server, daemon=True).start()
    
    print("Launching Secured Gost HTTPS proxy engine on port 8080...")
    
    # REVERTED TO http:// because Render handles the outer HTTPS/TLS termination for us
    subprocess.run(["/gost", "-L", "http://JadianRadiator:Majicka500akcijaM@:8080"]
