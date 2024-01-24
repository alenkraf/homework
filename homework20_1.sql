-- Create the table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(250) NOT NULL,
    book_author VARCHAR(250) NOT NULL
);

-- Rename the table
ALTER TABLE books
RENAME TO lib_books;

-- Add a new column to the table
ALTER TABLE lib_books
ADD COLUMN book_year INTEGER NULL;

-- Insert data into the table
INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book1', 'Author1', 1900);

INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book2', 'Author2', 1800);

INSERT INTO lib_books (book_name, book_author, book_year)
VALUES ('Book3', 'Author3', 1700);

-- Update a specific record
UPDATE lib_books
SET book_year = 2000
WHERE book_id = 2;

-- Delete records based on a condition
DELETE FROM lib_books
WHERE book_year = 1700;

-- Display the content of the table
SELECT * FROM lib_books;
