import os

import jinja2
import webapp2
import string

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render('homepage.html')


class Listi(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items = items)


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get("n", 0) # here 0 is for default value
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)

class ROT(Handler):
    def get(self):
        self.render("rot13.html")

    def post(self):
        rot = self.request.get("rot")
        rot13 = ''
        if rot:
            rot13 = rot.encode('rot13')
        self.render("rot13.html",rot=rot13)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/shopping_list', Listi),
                               ('/rot', ROT),
                               ('/fizzbuzz', FizzBuzzHandler)], debug=True)
