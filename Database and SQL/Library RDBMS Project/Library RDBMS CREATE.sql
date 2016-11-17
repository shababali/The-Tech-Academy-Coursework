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


