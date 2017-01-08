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
            if self.path.endswith("/restaurant/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data'
                        action='/restaurant/new'><h2>Name of the restaurant
                        </h2><input name="message" type="text" >
                        <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                # print output
                return

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
                    output += "<a href='/restaurant/"+str(i.id)+"/edit'>edit</a>" +"<br>"
                    output += "<a href='/restaurant/"+str(i.id)+"/delete'>delete</a>" +"<br><br>"
                output += "<br><br>"
                output += "<a href='/restaurant/new'>create new restaurant</a>"
                output += "</body></html>"
                self.wfile.write(output)
                # print output
                return

            if self.path.endswith("/edit"):
                restaurantid = self.path.split("/")[2]
                restaurantq = session.query(Restaurant).filter_by(id=restaurantid).one()
                if restaurantq:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += restaurantq.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/restaurant/%s/edit' >" % restaurantid
                    output += "<input name = 'newRestaurantName' type='text' placeholder = '%s' >" % restaurantq.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                    return

            if self.path.endswith("/delete"):
                restaurantid = self.path.split("/")[2]
                print restaurantid
                restaurantq = session.query(Restaurant).filter_by(id=restaurantid).one()
                print restaurantq
                if restaurantq:
                    session.delete(restaurantq)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()
                    return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:

            if self.path.endswith("/restaurant/new"):
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
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()
                    return

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantid = self.path.split("/")[2]
                    restaurantq = session.query(Restaurant).filter_by(id=restaurantid).one()
                    if restaurantq:
                        restaurantq.name = messagecontent[0]
                        session.add(restaurantq)
                        session.commit()
                        # redirect shown as udacity class
                        # instead of what i used above
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurant')
                        self.end_headers()
                        return



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
