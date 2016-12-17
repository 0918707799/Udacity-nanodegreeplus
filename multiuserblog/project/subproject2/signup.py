import os

import re
from string import letters

import jinja2
import webapp2
import string
import re
import random

from google.appengine.ext import db

import hashlib
import hmac

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

SECRET ="donot"
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    a= h.split("|")[0]
    if (h==make_secure_val(a)):
        return a

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

def user_key(name = 'default'):
    return db.Key.from_path('blogs', name)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class Userinfo(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.EmailProperty(required = True)
    def render(self):
        self._render_text = self.email.replace('\n', '<br>')
        return render_str("post.html", p = self)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class SignUp(Handler):
    def get(self):
        self.render("homepage.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_passwordord'] = "That wasn't a valid passwordord."
            have_error = True
        elif (password != verify):
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('homepage.html', **params)
        else:
            ## add cookies
            self.response.headers['Content-Type'] = 'text/plain'
            username_cookie_st = self.request.cookies.get('name')
            if username_cookie_st:
                username_val = check_secure_val(username_cookie_st)

            new_cookie_val = make_secure_val(str(username))
            self.response.headers.add_header('Set-Cookie', 'name=%s; path=/' % new_cookie_val)

            #encrypt hash password
            e_password = make_pw_hash(username, password)
            # create database
            uinfo = Userinfo(parent = user_key(), username = username, password = e_password, email = email)
            uinfo.put()

            self.redirect('/welcome?username=' + username)

class Front(Handler):
    def get(self):
        self.render('trial.html')

class Welcome(Handler):
    def get(self):
        user_name = self.request.get('username')
        self.render("welcome.html",username=user_name)




app = webapp2.WSGIApplication([('/signup', SignUp),
                               ('/?', Front),
                               ('/welcome',Welcome)], debug=True)


## to delete all data from database
# dev_appserver.py --clear_datastore=yes /home/bittu/Documents/github/Udacity/multiuserblog/project/subproject/
