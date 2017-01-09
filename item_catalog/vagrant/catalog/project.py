from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Restaurant, Base, MenuItem

app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')


def Helloworld():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ""
    for i in items:
        output += i.name
        output += '<br>'
        output += i.price
        output += '<br>'
        output += i.description
        output += '<br><br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port =5000)
