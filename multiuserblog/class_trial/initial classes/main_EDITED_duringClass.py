import webapp2

form = """
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
"""

# This is showing get method, which will usually used to get data from user or input
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

## This is showing post method, which is usually used to return or post something
#class TestHandler(webapp2.RequestHandler):
#    def post(self):
#        #q = self.request.get("q")
#        #self.response.out.write(q)
#
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write(self.request)


#app = webapp2.WSGIApplication([('/', MainPage),('/testform', TestHandler)],
#                            debug=True)


app = webapp2.WSGIApplication([('/', MainPage)],
                           debug=True)


####################################
check proper birthdate
import webapp2

form = """
<form method="post">
    What is your BirthDay?
    <br>

    <input type="text" name="month" >
    <input type="text" name="day" >
    <input type="text" name="year" >
    <br>
    <br>
    <input type="submit">
</form>
"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    month=month.title()
    if month in months:
        return month

def valid_day(day):
    if day and day.isdigit():
        day=int(day)
        if (0<day<32):
            return day

def valid_year(year):
    if year and year.isdigit():
        year=int(year)
        if (1900<year<2017):
            return year

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not(user_month and user_day and user_year):
            self.response.write(form)
        else:
            self.response.write("Thanks! that is correct input")


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
