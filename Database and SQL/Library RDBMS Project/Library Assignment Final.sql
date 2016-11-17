/*--------------------------------------
   SQL DRILL: LIBRARY DATABASE DESIGN
           AND QUERY SOLTIONS
---------------------------------------*/


/*The library schema utilizes 3 KERNEL (REFERENCE) TABLES that are essential objects for a functioning 
library relational database management system:

1. LIBRARY_BRANCH (Repository for the books), 
2. BOOK (The physical content exchanged), and
3. BORROWER (patron taking books from the institution)  

  The other Tables are attributes of the KERNELS: 
   
	BOOK - PUBLISHER, BOOK AUTHOR, BOOK_COPIES, BOOK_LOANS
	LIBRARY_BRANCH - BOOK_COPIES, BOOK_LOANS
	BORROWER - BOOK_LOANS 

	Certain attributes values facilitate methods for linking data indexes, whith concomitant 
	separation of data into a system of related data tables that are semantic. Some examples of these semantic 
	features are:
	- limiting data dipslay to not convolute a table eg separate publisher data from inventory data,
	- accessing meaningful information directly from data table values eg copies of books in a particular branch, 
	- security of sensitive values such as separating borrower name and address from a book loan. 
	etc.
*/


  /* CREATING LIBRARY DATABASE 
-------------------------------*/
USE MASTER
GO

IF  EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'dbLibrarySA')
DROP DATABASE [dbLibrarySA]
GO

CREATE DATABASE [dbLibrarySA]
GO

USE dbLibrarySA
GO 


  /* CREATING TABLES AND INDEXING PRIMARY-FOREIGN KEY RELATIONSHIPS
--------------------------------------------------------------------*/


CREATE TABLE BOOK --Refference Table
(
BookID int NOT NULL PRIMARY KEY,
Title varchar (50) NOT NULL,
PublisherID int NOT NULL --Semantic Change to SQL Drill Library Schema :- Add foreign key PublisherID that constrains relationship to Table PUBLISHER 
)
GO


CREATE TABLE LIBRARY_BRANCH --Refference Table
(
BranchID int NOT NULL PRIMARY KEY,
BranchName varchar (50) NOT NULL,
LBAddress varchar (100) NOT NULL
)
GO


CREATE TABLE BORROWER --Refference Table
(
CardNo int NOT NULL PRIMARY KEY,
LastName varchar (50) NOT NULL,
FirstName varchar (50) NOT NULL,--Semantic Change to SQL Drill Library Schema :- Separate Borrower Last Name and First Name
BrAddress varchar (100) NOT NULL,
BrPhone varchar (25) NOT NULL
)
GO


			CREATE TABLE PUBLISHER 
			(
			PublisherID int NOT NULL PRIMARY KEY, --Inclusion of a semantic primary key PublisherID
			PublisherName varchar (50) NOT NULL,  
			PubAddress varchar (100) NOT NULL,
			PubPhone varchar (25) NOT NULL
			)
			GO

	ALTER TABLE BOOK 
	ADD CONSTRAINT fk_PerBOOK
	FOREIGN KEY (PublisherID) REFERENCES PUBLISHER(PublisherID) --Relates Table PUBLISHER (JOIN ON PublisherID) back to Table BOOK


		CREATE TABLE BOOK_AUTHORS 
		(
		BookID int NOT NULL,   
		AuthorLastName varchar (50) NOT NULL, --Semantic Change to SQL Drill Library Schema :- Separate Author Last Name and First Name
		AuthorFirstName varchar (50) NOT NULL,
		CONSTRAINT fk_PerBOOK_AUTHORS 
		FOREIGN KEY (BookID) REFERENCES BOOK(BookID) --Relates Table BOOK_AUTHORS (JOIN ON BookID) back to Table BOOK
		)
		GO


		CREATE TABLE BOOK_COPIES 
		(						 
		BookID int NOT NULL, 
		BranchID int NOT NULL,			 
		No_of_Copies int NOT NULL,
		CONSTRAINT fk_PerBOOK_COPIES		
	    FOREIGN KEY (BookID) REFERENCES BOOK(BookID), --Relates Table BOOK_COPIES (JOIN ON BookID) back to Table BOOK
		FOREIGN KEY (BranchID) REFERENCES LIBRARY_BRANCH(BranchID) --Relates Table BOOK_COPIES (JOIN ON BranchID) back to Table LIBRARY_BRANCH
		)
		GO

		
		CREATE TABLE BOOK_LOANS 
		(						
		BookID int NOT NULL, 
		BranchID int NOT NULL,			 
		CardNo int NOT NULL,
		DateOut date NOT NULL, --date data type format is YYYY-MM-DD.
		DueDate date NOT NULL,
		CONSTRAINT fk_PerBOOK_LOANS	  
		FOREIGN KEY (BookID) REFERENCES BOOK(BookID), --Relates Table BOOK_LOANS (JOIN ON BookID) back to Table BOOK
		FOREIGN KEY (BranchID) REFERENCES LIBRARY_BRANCH(BranchID), --Relates Table BOOK_LOANS (JOIN ON BranchID) back to Table LIBRARY_BRANCH
		FOREIGN KEY (CardNo) REFERENCES BORROWER(CardNo) --Relates Table BOOK_LOANS (JOIN ON CardNo) back to Table BORROWER
		)
		GO

		
/*SCRIPT FOR INSERTING VALUES: into the constructed Library Database: 
-------------------------------
see SQL_Library_Drill.pdf file for assignment values*/
			

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

(1, 1, 1, '2016-11-01', '2016-12-01'),
(2, 1, 1, '2016-11-01', '2016-12-01'),
(3, 1, 1, '2016-11-01', '2016-12-01'),
(4, 1, 1, '2016-11-01', '2016-12-01'),
(5, 1, 1, '2016-11-07', '2016-12-07'),
(6, 1, 1, '2016-11-07', '2016-12-07'),
(7, 1, 2, '2016-11-08', '2016-12-08'),
(8, 1, 2, '2016-11-09', '2016-12-09'),
(9, 1, 2, '2016-11-09', '2016-12-09'),
(10, 1, 2, '2016-11-01', '2016-12-01'),
(1, 2, 4, '2016-11-07', '2016-12-07'),
(2, 2, 4, '2016-11-07', '2016-12-07'),
(3, 2, 4, '2016-11-07', '2016-12-07'),
(4, 2, 4, '2016-11-07', '2016-12-07'),
(5, 2, 4, '2016-11-07', '2016-12-07'),
(6, 2, 4, '2016-11-07', '2016-12-07'),
(7, 2, 5, '2016-11-07', '2016-12-07'),
(8, 2, 5, '2016-11-07', '2016-12-07'),
(9, 2, 5, '2016-11-08', '2016-12-08'),
(10, 2, 5, '2016-11-08', '2016-12-08'),
(1, 3, 6, '2016-11-07', '2016-12-07'),
(2, 3, 6, '2016-11-07', '2016-12-07'),
(3, 3, 6, '2016-11-07', '2016-12-07'),
(4, 3, 6, '2016-11-07', '2016-12-07'),
(5, 3, 6, '2016-11-07', '2016-12-07'),
(6, 3, 6, '2016-11-07', '2016-12-07'),
(7, 3, 7, '2016-11-07', '2016-12-07'),
(8, 3, 7, '2016-11-07', '2016-12-07'),
(9, 3, 7, '2016-11-08', '2016-12-08'),
(10, 3, 7, '2016-11-08', '2016-12-08'),
(11, 1, 1, '2016-11-02', '2016-12-02'),
(12, 1, 1, '2016-11-02', '2016-12-02'),
(13, 1, 1, '2016-11-02', '2016-12-02'),
(14, 1, 1, '2016-11-02', '2016-12-02'),
(15, 1, 1, '2016-11-02', '2016-12-02'),
(16, 2, 4, '2016-11-02', '2016-12-02'),
(17, 2, 4, '2016-11-02', '2016-12-02'),
(18, 2, 4, '2016-11-02', '2016-12-02'),
(19, 2, 4, '2016-11-03', '2016-12-03'),
(20, 2, 4, '2016-11-03', '2016-12-03'),
(11, 3, 6, '2016-11-08', '2016-12-08'),
(12, 3, 6, '2016-11-08', '2016-12-08'),
(13, 4, 6, '2016-11-09', '2016-12-09'),
(14, 4, 6, '2016-11-09', '2016-12-09'),
(15, 4, 6, '2016-11-09', '2016-12-09'),
(16, 4, 7, '2016-11-09', '2016-12-09'),
(17, 4, 7, '2016-11-09', '2016-12-09'),
(18, 3, 7, '2016-11-10', '2016-12-10'),
(19, 3, 7, '2016-11-10', '2016-12-10'),
(20, 3, 7, '2016-11-10', '2016-12-10')
GO

--8. There are at least 50 loans in the BOOK_LOANS table.


/*SCRIPT FOR INSERTING VALUES: into the constructed Library Database: 
-------------------------------
see SQL_Library_Drill.pdf file for assignment values*/


/* 1. How many copies of the book titled The Lost Tribe are owned 
by the library branch whose name is"Sharpstown"? */ 

SELECT BC.BranchID, LB.BranchName, BC.No_of_Copies
FROM BOOK AS B
FULL JOIN BOOK_COPIES AS BC ON B.BookID = BC.BookID
FULL JOIN LIBRARY_BRANCH AS LB ON BC.BranchID = LB.BranchID
WHERE B.Title = 'The Lost Tribe' AND LB.BranchName = 'Sharpstown'


/* 2. How many copies of the book titled The Lost Tribe are owned by 
each library branch?*/

SELECT BC.BranchID, LB.BranchName, BC.No_of_Copies
FROM BOOK AS B
FULL JOIN BOOK_COPIES AS BC ON B.BookID = BC.BookID
FULL JOIN LIBRARY_BRANCH AS LB ON BC.BranchID = LB.BranchID
WHERE B.Title = 'The Lost Tribe' 


/* 3. Retrieve the names of all borrowers who do not have any books 
checked out.*/

SELECT Br.CardNo, Br.LastName, Br.FirstName  
FROM BORROWER AS Br
FULL JOIN BOOK_LOANS AS BL ON Br.CardNo = BL.CardNo
WHERE BL.DueDate IS NULL  

/*The RDBMS doesn't allow inserting null values for dates in the BOOK_LOANS Table. Therefore, the null value ARGUMENT
for the DueDate PARAMETER, given our CLAUSES, in this query is effective.*/  


/* 4. For each book that is loaned out from the "Sharpstown" branch 
and whose DueDate is today, retrieve the book title, the borrower's 
name, and the borrower's address.*/

SELECT B.Title, Br.LastName, Br.FirstName, BrAddress, DueDate 
FROM BOOK_LOANS AS BL
FULL JOIN BOOK AS B ON BL.BookID = B.BookID
FULL JOIN LIBRARY_BRANCH AS LB ON BL.BranchID = LB.BranchID
FULL JOIN BORROWER AS Br ON BL.CardNo = Br.CardNo
WHERE LB.BranchName = 'Sharpstown' AND BL.DueDate = CONVERT (date,GETDATE())


/* 5. For each library branch, retrieve the branch name and the total 
number of books loaned out from that branch.*/

SELECT LB.BranchName, COUNT(BL.BookID) AS TotalBooksLoanedOut  
FROM BOOK_LOANS AS BL 
FULL JOIN LIBRARY_BRANCH AS LB ON BL.BranchID = LB.BranchID
WHERE BL.DueDate IS NOT NULL  
GROUP BY LB.BranchName
 

/* 6. Retrieve the names, addresses, and number of books checked 
out for all borrowers who have more than five books checked out*/

SELECT Br.LastName, Br.FirstName, Br.BrAddress, COUNT(BL.BookID) AS TotalBookLoans 
FROM BOOK_LOANS AS BL
FULL JOIN BORROWER AS Br ON BL.CardNo = Br.CardNo
WHERE BL.DueDate IS NOT NULL
GROUP BY Br.LastName, Br.FirstName, Br.BrAddress
HAVING COUNT(BL.BookID) > 5 


/* 7. For each book authored (or co-authored) by "Stephen King", 
retrieve the title and the number of copies owned by the 
library branch whose name is "Central"*/

SELECT B.Title, BC.No_of_Copies 
FROM BOOK AS B
FULL JOIN BOOK_COPIES AS BC ON BC.BookID = B.BookID
FULL JOIN BOOK_AUTHORS AS BA ON B.BookID = BA.BookID
FULL JOIN LIBRARY_BRANCH AS LB ON BC.BranchID = LB.BranchID
WHERE LB.BranchName = 'Central' AND BA.AuthorLastName = 'King' AND BA.AuthorFirstName = 'Stephen'
GO

/*Create a stored procedure that will execute one or more of those queries, based on user
choice. The following procedure retreives names, addresses, and number of books checked 
out for all borrowers with a user defined last name input. Command is EXEC uspGetLoans "letters in last name". 
The broad procedure returns all values given use of the null wildcard.*/


USE dbLibrarySA  
GO  
IF OBJECT_ID('uspGetLoans', 'P') IS NOT NULL  
    DROP PROCEDURE uspGetLoans  
GO 

CREATE PROCEDURE uspGetLoans @LastName varchar(30) = NULL
AS
SELECT Br.LastName, Br.FirstName, Br.BrAddress, COUNT(BL.BookID) AS TotalBookLoans 
FROM BOOK_LOANS AS BL
FULL JOIN BORROWER AS Br ON BL.CardNo = Br.CardNo
WHERE LastName LIKE '%' + ISNULL(@LastName,LastName) + '%'
GROUP BY Br.LastName, Br.FirstName, Br.BrAddress, Br.BrPhone
GO

EXEC uspGetLoans --Insert values for a name--
GO



