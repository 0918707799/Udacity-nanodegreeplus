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
    del_match.execute("delete from winning")
    db.commit()
    db.close()
    # print ("table for matches has been deleted")



def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    del_player = db.cursor()
    del_player.execute("delete from player")
    db.commit()
    db.close()
    # print ("table for players has been deleted");


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from player")
    count =  c.fetchall()[0][0]
    db.close()
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
    # print ("player added");


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
    db_player.execute("select * from playerstand")
    posts = db_player.fetchall()
    db.close()
    return posts


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    report = db.cursor()
    report.execute("INSERT into winning (winner, loser) values (%s, %s);", (winner, loser,))
    db.commit()
    db.close()
    # print ("record added");



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
    db = connect()
    pair = db.cursor()
    pair.execute("select * from playerstand")
    pairr =  pair.fetchall()
    # print pairr
    pair.execute("select count(*) from player")
    total_player = pair.fetchall()[0][0]
    # print total_player
    db.close()
    pairing = []
    for player in range(0, int(total_player),2):
        a_id = pairr [player][0]
        a_name = pairr [player][1]
        b_id = pairr [player+1][0]
        b_name = pairr [player+1][1]
        pairing.append((a_id, a_name, b_id, b_name))
    # print pairing
    return pairing
