from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Please use Streamlit Cloud for this app instead of Vercel. Vercel does not support Streamlit apps directly.'.encode())
        return
