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
                    match_id serial primary key,
                    winner integer,
                    loser integer,
                    foreign key (winner) references player (player_id),
                    foreign key (loser) references player (player_id)
);

CREATE VIEW playerstand AS
    select player.player_id as pl_id, player.playername,
    (select count(*) from winning where winning.winner = player.player_id) as win,
    (select count(*) from winning where player.player_id = winning.winner or player.player_id = winning.loser) as total_match
    from player group by player.player_id order by win desc;
