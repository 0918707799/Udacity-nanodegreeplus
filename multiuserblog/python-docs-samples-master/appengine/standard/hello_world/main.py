# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2

form = """
<form method="post">
    What is your BirthDay?
    <br>
    <label>month
    <input type="text" name="month" value="%(month)s" >
    </label>
    <label>day
    <input type="text" name="day" value="%(day)s" >
    </label>
    <label>year
    <input type="text" name="year" value="%(year)s" >
    </label>
    <br>
    <div style ="color:red">%(error)s</div>
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
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {"error": error,
                                        "month": month,
                                        "day": day,
                                        "year": year})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("That is wrong input", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! that is correct input")



app = webapp2.WSGIApplication([('/', MainPage),('/thanks',ThanksHandler)], debug=True)
