
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    contents text,
    views int,
-- The foreign key name is always {other_table_singular}_id
    account_id int
    -- constraint fk_account foreign key(account_id)
    --     references accounts(id)
    --     on delete cascade
);

INSERT INTO accounts (username, email) VALUES ('andrew', 'andrew@andrew.net');
INSERT INTO accounts (username, email) VALUES ('zarei', 'zarei@zarei.net');

INSERT INTO posts (title, contents, views, account_id) VALUES ('My Title 1', 'My Content 1', 0, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('My Title 2', 'My Content 2', 0, 2);

