# simple implementation of variable with jinja2
# with title and input text box
# datatype for the database (in google app datastore) - int, float, string, text, date, time, datetime
# properties in the google app datastore - email, link , postal address

import os

import jinja2
import webapp2

# for the database
from google.appengine.ext import db

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

class Art(db.Model):
    title = db.StringProperty(required = True) # required=True means this can't be blank, here
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * from Art ORDER BY created desc")

        self.render("home.html", title=title, art=art, error=error, arts=arts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")


class BlogCreatePage(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * from Art ORDER BY created desc")
        self.render("firstpage.html", title=title, art=art, error=error, arts=arts)

    def render_post(self, title="", art=""):
        arts = db.GqlQuery("SELECT * from Art ORDER BY created desc")
        self.render("blogpage.html", title=title, art=art)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()
            self.render_post(title, art)
        else:
            error = "Something is Missing"
            self.render_front(title, art, error)

class Blog(Handler):
    def get(self):
        arts = db.GqlQuery("SELECT * from Art ORDER BY created desc")
        n = self.request.get("n")
        for i in arts:
            if i.title==n:
                arty=i.art
                self.render("blogpage.html", title=n, art=arty)




app = webapp2.WSGIApplication([('/', MainPage),
                            ('/new',BlogCreatePage),
                            ('/blog',Blog)], debug=True)
