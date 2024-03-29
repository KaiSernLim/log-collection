import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Serve index.html for the root path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
