from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import json

jokeProviderUrl = "http://provider:3001"
serverPort = 5002

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>LB 347 Funny Joke</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>M347 Joke Consumer</h1>", "utf-8"))
        self.wfile.write(bytes("<p>"+joke+"</p>", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":   
    response = urlopen(jokeProviderUrl)
    data_json = json.loads(response.read())
    joke = data_json["joke"]     
    webServer = HTTPServer(("", serverPort), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")