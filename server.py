# server.py
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# List of specific environment variables to display
ENV_VARS_TO_DISPLAY = ["EXAMPLE_ENV_VAR", "ANOTHER_ENV_VAR"]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        env_vars = {key: os.getenv(key) for key in ENV_VARS_TO_DISPLAY if os.getenv(key) is not None}
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Environment Variables</title>
        </head>
        <body>
            <h1>Environment Variables</h1>
            <pre>{env_vars}</pre>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
