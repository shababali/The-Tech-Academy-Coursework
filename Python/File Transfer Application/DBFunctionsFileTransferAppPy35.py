
# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Use Python, Tkinter library (Python GUI) and Python modules to build a file-transferring application with database
#                 activity tracking utility. The following script acts as a database module for SQLite functions called by the 
#                 File Transfer Application. 
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.


import datetime
import time
import sqlite3


'''DATABASE FUNCTIONS'''


# Establishes connection with database, and creates the table if it does not already exist
# DATABASE NAME: FileTransferApplication.db
# TABLE NAME: DBtransfertimestamps
# FIELDS: (unix REAL) ie DBtransfertimestamps has one column called unix that stores values of REAL datatype.


def createDB():

    conn = sqlite3.connect('FileTransferApplication.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS DBtransfertimestamps(unix REAL)")
        c.execute("SELECT COUNT(*) FROM DBtransfertimestamps")
        count = c.fetchone()[0]
        if count < 1:
                c.execute("INSERT INTO DBtransfertimestamps VALUES(((julianday('now') - 2440587.5)*86400.0)-86400.0)")#inserts a default 24 hours previous day timestamp into a novel program instance.         
        conn.commit()                                                                                               # timestamp is in unix (seconds since epoch)
        c.close()
    conn.close()


# Reads the max unix value from the timestamps table, and populates the tkinter label widget
    

def readDB():
        
    conn = sqlite3.connect('FileTransferApplication.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(unix) FROM DBtransfertimestamps")
        lastTransfer = c.fetchone()[0]
        read_lastTransfer = time.ctime(lastTransfer)
        conn.commit()    
        
    return lastTransfer

# Inserts a TIMESTAMP unvalue into the timestamps table, and records a file transfer event, when called
# by the fileMove function.

def FileTransfer_TIMESTAMP():
        
    conn = sqlite3.connect('FileTransferApplication.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO DBtransfertimestamps VALUES((julianday('now') - 2440587.5)*86400.0)") # inserts a new timestamp (into TABLE) in unix (seconds since epoch)
        conn.commit()
        c.close()
    conn.close()







