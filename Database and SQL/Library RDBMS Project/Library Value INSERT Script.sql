
USE dbLibrarySA
GO


INSERT INTO PUBLISHER --(PublisherID, PublisherName, PubAddress, PubPhone)
VALUES 
(1, 'Smith Publishing House', 'PO Box 123', '503-123-5555'),
(2, 'Penguin Random House', '1331 1st St Portland OR 97124', '503-234-5555'),
(3, 'Simon & Schuster', '333 Grant St Portland OR 97015', '503-354-5552'),
(4, 'HarperCollins', '444 3rd Ave Portland OR 97232', '503-555-5555'),
(5, 'Pearson', 'PO Box 565', '503-685-3744'),
(6, 'ThomsonReuters', '1331 31st St Portland OR 97121', '503-780-1516'),
(7, 'Wiley', '545 Division St Portland OR 97015', '503-788-7675')

GO

INSERT INTO BOOK --(BookID, Title, PublisherID)
VALUES 

(1, 'A Scanner Darkly', 5),	 
(2, 'Shall not Perish', 1),	
(3, 'The Skull Beneath the Skin', 7),
(4, 'The Soldiers Art', 3),	  
(5, 'Master and Commander', 4),
(6, 'Gotcha', 5),
(7, 'Lolita', 2),
(8, 'Haha', 1),
(9, 'Antitrust and American Business Abroad', 6),
(10, 'Carrie', 3),
(11, 'The Lost Tribe', 7), --1. There is a book called 'The Lost Tribe'
(12, 'The Lost World', 5),
(13, 'The Shining', 3),
(14, 'IT', 3),
(15, 'A Game of Thrones', 2),
(16, 'A Storm of Swords', 2),
(17, 'A Feast of Crows', 2),
(18, 'A Dance of Dragons', 2),
(19, 'A Clash of Kings', 2),
(20, 'Heart of Darkness', 4) --3. There are at least 20 books in the BOOK table
GO

INSERT INTO BOOK_AUTHORS --(BookID, AuthorLastName, AuthorFirstName)
VALUES 
(1, 'Dick', 'Philip'),
(2, 'Faulkner', 'William '),
(3, 'James', 'Phyllis D.'),
(4, 'Powell', 'Anthony'),
(5, 'OBrian', 'Patrick'),
(6, 'Talor', 'Eldon'),
(7, 'Nabokov', 'Vladimir'),
(8, 'King', 'David'),
(9, 'Fiebig', 'Andre'),
(10, 'King', 'Stephen'),
(11, 'Mann', 'Michael'),
(12, 'Doyle', 'Conan'),
(13, 'King', 'Stephen'),
(14, 'King', 'Stephen'), --9. There must be at least one book written by 'Stephen King'.
(15, 'Martin', 'George RR'),
(16, 'Martin', 'George RR'),
(17, 'Martin', 'George RR'),
(18, 'Martin', 'George RR'),
(19, 'Martin', 'George RR'),
(20, 'Conrad', 'Joseph') --4. There are at least 10 authors in the BOOK_AUTHORS table.
GO

INSERT INTO LIBRARY_BRANCH --(BranchID, BranchName, LBAddress)
VALUES 
(1, 'Sharpstown', '747 26th Ave Portland OR 97233'),
(2, 'Central', '111 Sandy Blvd Portland OR 97035'), -- 2. There is a library branch called 'Sharpstown' and one called 'Central'.
(3, 'Alberta', '122 Missisipi Ave Portland OR 97123'),
(4, 'Belmont', '1038 SE Cesar E Chavez Blvd Portland OR 97214')
GO --7. There are at least 4 branches in the LIBRARY_BRANCH table.

INSERT INTO BORROWER --(CardNo, LastName, FirstName, BrAddress, BrPhone)
VALUES 
(1, 'Biles', 'Simone', '536 11th St Portland OR 97222', '503-456-4675'),
(2, 'Bolt', 'Usain', '432 Whyte Ave Portland OR 97222', '503-899-9434'),
(3, 'Phelps', 'Michael', '253 Willow Ave Portland OR 97223', '503-932-2341'),
(4, 'Johnson', 'Ben', '111 Oak Ave Portland OR 97223', '503-984-1982'),
(5, 'Kwan', 'Michelle', '908 Seymour St Portland OR 97014', '503-985-1565'),
(6, 'Allen', 'Linda', '807 Sexton St Portland OR 97036', '503-983-4398'),
(7, 'Lewis', 'Carl', '32 Angels Blvd Portland OR 97155', '503-444-6889'),
(8, 'Paige', 'Becky', '655 Broughton Ave Portland OR 97232', '503-238-3425'),
(9, 'Samson', 'Erin', '543 Tabor Lane Portland OR 97233', '503-532-4255'),
(10, 'Flanagan', 'Shalane', '346 5th Ave Portland OR 97124', '503-784-5458')
GO

/* 6. There are at least 8 borrowers in the BORROWER table, 
and at least 2 of those borrowers have more
than 5 books loaned to them...see BOOK_LOANS */

INSERT INTO BOOK_COPIES --(BookID, BranchID, No_of_Copies)
VALUES 
(1, 1, 2),
(1, 2, 2),
(1, 3, 2),
(1, 4, 2),
(2, 1, 2),
(2, 2, 2),
(2, 3, 2),
(2, 4, 2),
(3, 1, 2),
(3, 2, 2),
(3, 3, 2),
(3, 4, 2),
(4, 1, 2),
(4, 2, 2),
(4, 3, 2),
(4, 4, 2),
(5, 1, 2),
(5, 2, 2),
(5, 3, 2),
(5, 4, 2),
(6, 1, 2),
(6, 2, 2),
(6, 3, 2),
(6, 4, 2),
(7, 1, 2),
(7, 2, 2),
(7, 3, 2),
(7, 4, 2),
(8, 1, 2),
(8, 2, 2),
(8, 3, 2),
(8, 4, 2),
(9, 1, 2),
(9, 2, 2),
(9, 3, 2),
(9, 4, 2),
(10, 1, 2),
(10, 2, 2),
(10, 3, 2),
(10, 4, 2),
(11, 1, 2),
(11, 2, 2),
(11, 3, 2),
(11, 4, 2),
(12, 1, 2),
(12, 2, 2),
(12, 3, 2),
(12, 4, 2),
(13, 1, 2),
(13, 2, 2),
(13, 3, 2),
(13, 4, 2),
(14, 1, 2),
(14, 2, 2),
(14, 3, 2),
(14, 4, 2),
(15, 1, 2),
(15, 2, 2),
(15, 3, 2),
(15, 4, 2),
(16, 1, 2),
(16, 2, 2),
(16, 3, 2),
(16, 4, 2),
(17, 1, 2),
(17, 2, 2),
(17, 3, 2),
(17, 4, 2),
(18, 1, 2),
(18, 2, 2),
(18, 3, 2),
(18, 4, 2),
(19, 1, 2),
(19, 2, 2),
(19, 3, 2),
(19, 4, 2),
(20, 1, 2),
(20, 2, 2),
(20, 3, 2),
(20, 4, 2) 
GO	

/*--5. Each library branch has at least 10 book titles, 
and at least two copies of each of those titles.*/

INSERT INTO BOOK_LOANS --(BookID, BranchID, CardNo, DateOut, DueDate)
VALUES 

(1, 1, 1, '2016-10-01', '2016-11-01'),
(2, 1, 1, '2016-10-01', '2016-11-01'),
(3, 1, 1, '2016-10-01', '2016-11-01'),
(4, 1, 1, '2016-10-01', '2016-11-01'),
(5, 1, 1, '2016-10-01', '2016-11-01'),
(6, 1, 1, '2016-10-01', '2016-11-01'),
(7, 1, 2, '2016-10-01', '2016-11-01'),
(8, 1, 2, '2016-10-01', '2016-11-01'),
(9, 1, 2, '2016-10-01', '2016-11-01'),
(10, 1, 2, '2016-10-01', '2016-11-01'),
(1, 2, 4, '2016-10-07', '2016-11-07'),
(2, 2, 4, '2016-10-07', '2016-11-07'),
(3, 2, 4, '2016-10-07', '2016-11-07'),
(4, 2, 4, '2016-10-07', '2016-11-07'),
(5, 2, 4, '2016-10-07', '2016-11-07'),
(6, 2, 4, '2016-10-07', '2016-11-07'),
(7, 2, 5, '2016-10-07', '2016-11-07'),
(8, 2, 5, '2016-10-07', '2016-11-07'),
(9, 2, 5, '2016-10-08', '2016-11-08'),
(10, 2, 5, '2016-10-08', '2016-11-08'),
(1, 3, 6, '2016-10-07', '2016-11-07'),
(2, 3, 6, '2016-10-07', '2016-11-07'),
(3, 3, 6, '2016-10-07', '2016-11-07'),
(4, 3, 6, '2016-10-07', '2016-11-07'),
(5, 3, 6, '2016-10-07', '2016-11-07'),
(6, 3, 6, '2016-10-07', '2016-11-07'),
(7, 3, 7, '2016-10-07', '2016-11-07'),
(8, 3, 7, '2016-10-07', '2016-11-07'),
(9, 3, 7, '2016-10-08', '2016-11-08'),
(10, 3, 7, '2016-10-08', '2016-11-08'),
(11, 1, 1, '2016-10-02', '2016-11-02'),
(12, 1, 1, '2016-10-02', '2016-11-02'),
(13, 1, 1, '2016-10-02', '2016-11-02'),
(14, 1, 1, '2016-10-02', '2016-11-02'),
(15, 1, 1, '2016-10-02', '2016-11-02'),
(16, 2, 4, '2016-10-02', '2016-11-02'),
(17, 2, 4, '2016-10-02', '2016-11-02'),
(18, 2, 4, '2016-10-02', '2016-11-02'),
(19, 2, 4, '2016-10-03', '2016-11-03'),
(20, 2, 4, '2016-10-03', '2016-11-03'),
(11, 3, 6, '2016-10-08', '2016-11-08'),
(12, 3, 6, '2016-10-08', '2016-11-08'),
(13, 4, 6, '2016-10-09', '2016-11-09'),
(14, 4, 6, '2016-10-09', '2016-11-09'),
(15, 4, 6, '2016-10-09', '2016-11-09'),
(16, 4, 7, '2016-10-09', '2016-11-09'),
(17, 4, 7, '2016-10-09', '2016-11-09'),
(18, 3, 7, '2016-10-10', '2016-11-10'),
(19, 3, 7, '2016-10-10', '2016-11-10'),
(20, 3, 7, '2016-10-10', '2016-11-10')
GO

--8. There are at least 50 loans in the BOOK_LOANS table.

