from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbsetup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurant"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                items = session.query(Restaurant).all()
                for i in items:
                    # print i.name
                    output += i.name + "<br>"
                    output += "<a href='/edit'>edit</a>" +"<br>"
                    output += "<a href='/delete'>delete</a>"+"<br>"+"<br>"
                output += '''<form method='POST' enctype='multipart/form-data'
                        action='/restaurant'><h2>Name of the restaurant
                        </h2><input name="message" type="text" >
                        <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                # print output
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            # count =10
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
                xyz = messagecontent[0]
                print xyz + "  -- adding this"
                restaurant1 = Restaurant(name=xyz)
                session.add(restaurant1)
                session.commit()
            self.do_GET()
            # print output
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
