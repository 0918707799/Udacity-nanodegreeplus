#
# Database access functions for the web forum.
#

import time
import psycopg2
import bleach

## Database connection


## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
    bleach.clean(posts)
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("INSERT into posts (content) values (%s)", (content,))
    DB.commit()
    DB.close()


    # DO NOT TRY:
    # ');delete from posts;--
    # (this is called sql injection attack)
    # This code can delete our database if we use our insert query as following:
    # c.execute("INSERT into posts (content) values ('%s')", % content)
    # and also if we add ''quotes then it will an error
    # so to avoid this above correction in code is the solution



# This is simple spam code
# <script>
#     setTimeout(function() {
#         var tt = document.getElementById('content');
#         tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
#         tt.form.submit();
#         }, 2500);
# </script>
#
# your backend is done properly and server is securey done but this code can cause spam due to browser
# your web server and data server is treating this as a text but browser is interpriting with different meaning
#
# this is called script injection attack
# you can use python library named "Bleach" to get out of this scenario and save you web application form spam like this
#
# but data which has been already entered, you need to remove it or replace it
# update posts set content='cheese' where content like '%spam%';
# this update query on your database table will replace all damaged data done by script injection to cheese


# To delete the post use following query
# delete from posts where content='cheese';
