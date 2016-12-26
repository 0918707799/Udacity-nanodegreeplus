
import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()


# If you are working with data server on the network the,
# you may need to provide more parameters; such as id, password instead of
# just student in following line
# db = sqlite3.connect("students")

# If you are using insert wuery then do not forget to commit it
# c.execute("insert into balloons values ('blue', 'water') ")
# db.commit()
# If you do not commit then you inserting rolls back

# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
# query = "select name, id from students order by name order by name;"
