# simple implementation of variable with jinja2
# with title and input text box
# datatype for the database (in google app datastore) - int, float, string, text, date, time, datetime
# properties in the google app datastore - email, link , postal address

import os

import jinja2
import webapp2

# this libraries are for cookies and cookies authentication
import hashlib
import hmac

# for the database
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

# Implemented the function make_secure_val, which takes a string and returns a
# string of the format:
# s,HASH
SECRET ="donot" # do not share or publish this
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    a= h.split("|")[0]
    if (h==make_secure_val(a)):
        return a
    #or
    # if hash_str(a[0])==a[1]:
    #     return a[0]
    # else:
    #     return None

##### simple encryption algorith for the has value of passwork
# make_salt() function cretate random value
# and make_pw_hash() creates hash value of (name+psswd+salt)
def make_salt():
    return "".join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name+pw+salt).hexdigest()
    return "%s,%s" % (h, salt)

def valid_pw(name, pw, h):
    salt=h.split(",")[1]
    return h == make_pw_hash(name, pw, salt)

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
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visit_cookie_st = self.request.cookies.get('visits')
        if visit_cookie_st:
            cookie_val = check_secure_val(visit_cookie_st)
            if cookie_val:
                visits = int(cookie_val)

        visits += 1

        new_cookie_val = make_secure_val(str(visits))
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        if visits>100:
            self.write("you love me!!!")
        else:
            self.write("you've been here %s times!" % visits)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
