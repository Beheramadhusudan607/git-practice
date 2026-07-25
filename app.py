from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from Jenkins + Podman!")

        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Application is healthy!")

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Application running on port 8000")

server.serve_forever()