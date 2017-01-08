from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from exercise import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppies.db')


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# query1
items = session.query(Puppy).order_by(Puppy.name).all()
for i in items:
    print i.name

# query2
items = session.query(Puppy).filter(Puppy.dateOfBirth>= '2016-12-12')
for i in items:
    print i.name, ":" , i.dateOfBirth

# query3
items = session.query(Puppy).order_by(Puppy.weight.asc()).all()
for i in items:
    print i.name, i.weight

# query4
items = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
for item in items:
    print item[0].id, item[0].name, item[1]
