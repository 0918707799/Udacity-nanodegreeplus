# begininning of the file
# import all the required libraries

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declareative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declareative_base()





# at the end of the file

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
