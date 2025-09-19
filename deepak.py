from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>deepakkumar</title>
    </head>
    <body>
        <center>
        <h1>arun laptops(25016457)</h1>
        <table border="3">
        <tr>
            <th>NO</th>
            <th>Brand</th>
            <th>processer</th>
            <th>Graphic card</th>
        </tr>
        <tr>
            <td>1</td>
            <td>lenovo</td>
            <td>intel core i5</td>
            <td>intel uhd graphic</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Acer</td>
            <td>intel ultra 7</td>
            <td>intel graphic</td>
        </tr>
        <tr>
            <td>3</td>
            <td>lenovo</td>
            <td>intel core i5></td>
            <td>intel graphic</td>
        </tr>
        <tr>
            <td>4</td>
            <td>asus</td>
            <td>intel core is</td>
            <td> ryzen graphic</td>
        </tr>
        <tr>
            <td>5</td>
            <td>apple</td>
            <td>intel ultra 7</td>
            <td>graphic123</td>
        </tr>
        </table>
        </center>


    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()