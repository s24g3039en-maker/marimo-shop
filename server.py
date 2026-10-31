#!/usr/bin/env python3
"""
Marimo Shop - Web Server Script
0.0.0.0:80 で静的ファイルを配信する軽量Webサーバー
"""

import http.server
import socketserver
import os
import sys

PORT = 80
HOST = "0.0.0.0"
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # キャッシュ無効化とUTF-8指定のヘッダー追加
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    # ソケット再利用を許可
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        print(f"==================================================")
        print(f" Marimo Shop Web Server is running!")
        print(f" URL: http://{HOST}:{PORT}/")
        print(f" Document Root: {DIRECTORY}")
        print(f" Press Ctrl+C to stop.")
        print(f"==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
            sys.exit(0)

if __name__ == '__main__':
    run_server()
