-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR  'user_0d_2'@'localhost' = 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
GRANT SELECT ON 'hbtn_0d_2' TO 'user_0d_1'@'localhost';
