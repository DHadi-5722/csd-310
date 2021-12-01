DROP USER IF EXISTS 'pysports_user'@'localhost';
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQLIsGreat!';

GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

DROP TABLE IF EXISTS player;

CREATE TABLE team (
     team_id         INT         NOT NULL,   AUTO_INCREMENT,
     tean_name       VARCHAR(75)  NOT NULL,
     mascot          VARCHAR(75)  NOT NULL,
     PRIMARY KEY(team_id)
);
INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Green Dragons');
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');
CREATE TABLE player(
    player_id   INT          NOT NULL      AUTO_INCREMENT,
    first_name  VARCHAR(75)  NOT NULL,
    last_name   VARCHAR(75)  NOT NULL,
    team_id     INT          NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team_id)
        REFERENCES team(team_id)
);
INSERT INTO player(first_name, last_name)
    VALUES('Randy', 'Meyer');
INSERT INTO player(first_name, last_name)
    VALUES('Johnny', 'Meyer');
INSERT INTO player(first_name, last_name)
    VALUES('Wayne', 'Jefferson');
INSERT INTO player(first_name, last_name)
    VALUES('Sam', 'Adams');
INSERT INTO player(first_name, last_name)
    VALUES('John', 'Anasto');
INSERT INTO player(first_name, last_name)
    VALUES('Billy', 'Johnson');

SELECT * FROM team WHERE team_name = 'Team Sauron';
