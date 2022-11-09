
CREATE DATABASE IF NOT EXISTS hellotable;
use hellotable;

DROP TABLE IF EXISTS test_table;

CREATE TABLE test_table (
  word1 VARCHAR(200),
  word2 VARCHAR(200)
);

INSERT INTO test_table
  (word1, word2)
VALUES
  ('hello', 'world'),
  ('whats', 'up');
  
  
  
