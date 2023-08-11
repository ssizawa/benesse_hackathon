CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL UNIQUE,
    point INT(6) NOT NULL DEFAULT 0,
    question1 INT(6) NULL,
    question2 INT(6) NULL,
    question3 INT(6) NULL,
    question4 INT(6) NULL,
    question5 INT(6) NULL,
    question6 INT(6) NULL,
    question7 INT(6) NULL,
    question8 INT(6) NULL,
    question9 INT(6) NULL,
    question10 INT(6) NULL
);

INSERT INTO User(name, password, question1, question2, question3, question4, question5, question6, question7) VALUES
    ('izawa', 'qqq', 1, 2, 3, 1, 2, 1, 4),
    ('shin', 'aaa', 1, 5, 1, 2, 1, 2, 1),
    ('hashimoto', 'bbb', 3, 6, 4, 3, 1, 2, 4),
    ('wani', 'ccc', 2, 2, 3, 1, 2, 1, 3),
    ('satou', 'qwer', 2, 6, 4, 3, 2, 2, 5);

INSERT INTO User(name, password) VALUES
    ('kato', '123'),
    ('Hiroki', '111');