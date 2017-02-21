
# Python Version: Python 2.7.13
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn SQLite and Python.
#                 
#
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.


# 1. Create a database table in RAM named Roster that includes the fields Name,Species and IQ:

import sqlite3

connection=sqlite3.connect(":memory:")

with sqlite3.connect('Roster.db')as connection:
    c=connection.cursor()

    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT,Species TEXT,IQ INT)")


# 2. Populate your new table with the following values:
#   1 Jean-Baptiste Zorg, Human, 122
#   2 Korben Dallas, Meat Popsicle, 100
#   3 Ak'not, Mangalore, -5


rosterRecords=(
    ('Jean-Baptiste Zorg', 'Human',122),
    ('Korben Dallas','Meat Popsicle',100),
    ("Ak'not",'Mangalore',-5)
    )

c.executemany("INSERT INTO Roster VALUES(?,?,?)",rosterRecords)

print("Roster Table:")
c.execute("SELECT* FROM Roster")
for row in c.fetchall():
    print (row)
print ("")


# 3. Update the Species of Korben Dallas to be Human:

print ("Update 'Korben Dallas' SPECIES Type to 'Human':")
c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human', 'Korben Dallas', 100))

c.execute("SELECT* FROM Roster WHERE Name='Korben Dallas'")
for row in c.fetchall():
    print (row)
print ("")

# 4. Display the names and IQs of everyone in the table who is classified as 'Human':

print ("Records in Roster Table where Species Type is 'Human':")
c.execute("SELECT Name, IQ FROM Roster WHERE Species ='Human'")
for row in c.fetchall():
    print (row)
print("")


# Instead of fetching for all and viewing query results as tuples, evalate rows iteratively and
# generate a formatted view.

print ("ALTERNATIVE VIEW - Records in Roster Table where Species Type is 'Human': ")
print ("")
c.execute("SELECT Name, IQ FROM Roster WHERE SPECIES ='Human'")
while True:
    row=c.fetchone()
    if row is None:
        break
    print ("Name: {}, IQ: {}".format(row[0], row[1])) # name = first tuple value/first Roster TABLE field
                                                      # IQ = second tuple value/second Roster TABLE field 

