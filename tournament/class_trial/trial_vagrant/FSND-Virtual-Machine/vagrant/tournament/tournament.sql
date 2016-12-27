-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE player (
                    playername TEXT,
                    player_id SERIAL primary key
);

CREATE TABLE winning (
                    player_id SERIAL,
                    winnum integer
);

CREATE TABLE match (
                    winner SERIAL,
                    loser SERIAL,
                    match_id SERIAL
);
