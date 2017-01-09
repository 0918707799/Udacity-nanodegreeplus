# imported Flask class from flask library
from flask import Flask

# created instance(here "app") of Flask class
# created this instance with the name of the running application as an argument
# Any time we run an application special variable called "__name__"gets defined
# for the application and al the imports it uses
app = Flask(__name__)

# this is called decorator eg. @app.route
# this decorator essentially wraps our function inside the app.route function
# that flask has already created
@app.route('/')
@app.route('/hello')

# so either of the above routes get sent from the browser,..
# the function defined below gets executed
def Helloworld():
    return "Hello World"

# application run by python interpreter(here this pytohn script) gets name variable set to "__main__"
# where as all the other imported python files get a __name__ set to
# the actual name of the python file
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port =5000)
# basically this condition means, if you are running this script run statement under the condition
# but if you are importing this script then ignore this
