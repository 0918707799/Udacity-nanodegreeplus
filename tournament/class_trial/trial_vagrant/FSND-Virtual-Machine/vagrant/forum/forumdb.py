#
# Database access functions for the web forum.
#

import time
import psycopg2

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
