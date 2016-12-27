
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


# simple counting of row:('animals' table has species and food columns)
# select species, count(*) from animals group by species;
# This query will count howmany same species we have




# PRODUCTS:                               SALES:
# sku     price       name                sku     sale_date       count
# 101     $413        ab                  222     2009-04-13      4
# 222     $11.11      xy                  343     2010-05-31      1
# 343     $61.20      mn                  222     2011-11-11      4
# 1025    $0.33       op
# Products and Sales
# Suppose that we want to know how many times we have sold each product. In other words, for each sku value in the products table, we want to know the number of times it occurs in the sales table. We might start out with a query like this:
#
# select products.name, products.sku, count(*) as num
#   from products join sales
#     on products.sku = sales.sku
#   group by products.sku;
# But this query might not do exactly what we want. If a particular sku has never been sold — if there are no entries for it in the sales table — then this query will not return a row for it at all.
#
# If we wanted to see a row with the number zero in it, we’ll be disappointed!
#
# However, there is a way to get the database to give us a count with a zero in it. To do this, we’ll need to change two things about this query —
#
# select products.name, products.sku, count(sales.sku) as num
#   from products left join sales
#     on products.sku = sales.sku
#   group by products.sku;



######################
# document: https://www.postgresql.org/docs/9.4/static/sql-createdatabase.html
# to create postgresql database:
# create database fun;
# ##
# CREATE DATABASE name
#     [ [ WITH ] [ OWNER [=] user_name ]
#            [ TEMPLATE [=] template ]
#            [ ENCODING [=] encoding ]
#            [ LC_COLLATE [=] lc_collate ]
#            [ LC_CTYPE [=] lc_ctype ]
#            [ TABLESPACE [=] tablespace_name ]
#            [ CONNECTION LIMIT [=] connlimit ] ]


# to create table in postgresql database:
# create table funn(title varchar(40), date_time date);
# ##
# CREATE TABLE tablename(
#     column1 type [constrain],
#     column2 type [constrain],
#     .
#     .
#     .
#     );


# ######### Declaring primary key
# example1.if you have only one column as a primary key
# create table students (
#     id serial primary key,
#     name text,
#     birthdate date
# );

# example2. if you have more than one column as a primary key
# create table postal_places (
#     postal_code text,
#     country text,
#     name text,
#     primary key (postal_code, country)
# );



###
# Roommate Finder v0.9
#
# This query is intended to find pairs of roommates.  It almost works!
# There's something not quite right about it, though.  Find and fix the bug.
# "residence" table has 3 columns. id(student id),building(dorms' name), room(room no.)
# QUERY = '''
# select a.id, b.id, a.building, a.room
#       from residences as a, residences as b
#  where a.building = b.building
#   and a.room = b.room
#   and a.id < b.id
# '''



# ##subquery:
# Find the players whose weight is less than the average.
#
# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.
#
# example using two different query
# def lightweights(cursor):
#     """Returns a list of the players in the db whose weight is less than the average."""
#     cursor.execute("select avg(weight) as av from players;")
#     av = cursor.fetchall()[0][0]  # first column of first (and only) row
#     cursor.execute("select name, weight from players where weight < " + str(av))
#     return cursor.fetchall()
#
# example using subquery
# def lightweights(cursor):
#     """Returns a list of the players in the db whose weight is less than the average."""
#     cursor.execute("""select name, weight from players,
                            # (select avg(weight) as av from players) as sub
                            # where weight < sub.av
#                             """)
#     return cursor.fetchall()

# def lightweights(cursor):
#     """Returns a list of the players in the db whose weight is less than the average."""
#     cursor.execute("""select players.name, players.weight, sub.av
#                             from players join (select avg(weight) as av from players)sub
#                             where weight < sub.av
#                             """)
#     return cursor.fetchall()


# ##view
# if we are using same wuery many times then we can save that query and that is called view
# note: it i kinda function call instead of copying code
# Example table:
#
# Enrollment:
# student_id      course_id
# 123             CS101
# 234             B102
# 345             CS101
# 456             MATH245
#
# How manu students are enrolled in each course?
# create view course_size as
#     select course_id, count(*) as num
#         from Enrollment
#         group by course_id;
