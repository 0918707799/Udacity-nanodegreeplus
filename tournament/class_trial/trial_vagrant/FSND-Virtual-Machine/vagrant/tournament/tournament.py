#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    del_match = db.cursor()
    del_match.execute("delete from match")
    db.commit()
    db.close()
    print ("table for matches has been deleted")



def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    del_player = db.cursor()
    del_player.execute("delete from player")
    db.commit()
    db.close()
    print ("table for players has been deleted");


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from player")
    count =  c.fetchall()[0][0]
    db.close()
    print ("counting__", count)
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    add_player = db.cursor()
    add_player.execute("INSERT into player (playername) values (%s)", (name,))
    db.commit()
    db.close()
    print ("player added");


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    db_player = db.cursor()
    query ="""SELECT player.player_id, player.playername, winning.winnum
                FROM player left join winning
                on player.player_id = winning.player_id
                ORDER BY winning.winnum desc
    """
    db_player.execute(query)
    posts = ({'player_id': str(row[0]), 'name': str(row[1]), 'winning': str(row[2])} for row in db_player.fetchall())
    db.close()
    print (posts);


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    del_player = db.cursor()
    query ="INSERT into match (winner, loser) values (%s, %s);", (winner, loser,)
    del_player.execute(query)
    db.close()
    print ("record added");



def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
