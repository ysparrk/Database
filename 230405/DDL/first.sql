CREATE TABLE
contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- # ALTER TABLE
-- 1. Rename a table
-- table name contacts -> new_contacts로 바뀜
ALTER TABLE contacts RENAME TO new_contacts;

-- 2. Rename a column
-- column name -> last_name으로 바뀜
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
ALTER TABLE new_contacts RENAME COLUMN age TO new_age;

-- 3. Add a new column to a table
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
ALTER TABLE new_contacts ADD COLUMN empty TEXT NOT NULL;

-- 4. Delete a column
ALTER TABLE new_contacts DROP COLUMN address;
ALTER TABLE new_contacts DROP COLUMN empty;


-- ALTER TABLE new_contacts DROP COLUMN email
-- Cannet drop UNIQUE column: "email"

-- # DROP TABLE
DROP TABLE new_contacts;