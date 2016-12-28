-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP TABLE IF EXISTS player cascade;
DROP TABLE IF EXISTS winning cascade;



CREATE TABLE player (
                    playername TEXT,
                    player_id SERIAL primary key
);

CREATE TABLE winning (
                    match_id SERIAL primary key,
                    winner INTEGER,
                    loser INTEGER,
                    FOREIGN KEY (winner) REFERENCES player (player_id),
                    FOREIGN KEY (loser) REFERENCES player (player_id)
);

CREATE VIEW playerstand AS
    SELECT player.player_id as pl_id, player.playername,
    (SELECT count(*) FROM winning WHERE winning.winner = player.player_id) as win,
    (SELECT count(*) FROM winning WHERE player.player_id = winning.winner or player.player_id = winning.loser) as total_match
    FROM player GROUP BY player.player_id ORDER BY win desc;
