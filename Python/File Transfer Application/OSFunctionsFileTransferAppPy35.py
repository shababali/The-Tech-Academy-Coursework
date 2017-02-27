
# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python, Shutil module and OS module.
#                 Function Design and integration.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.


# The following script is a module that comprises the kernel Program Functions, utilizing OS module and Shutil module, for the File Transfer Application.   
# The Main Program should be executed through MAINFileTransferAppPy35.py

# Modified from a Daily File Transfer Script. Residual elements of original script have been left in for readability and trace value.
# Example, print statements to SHELL from function calls and FileCheck Function.


from tkinter import*
import tkinter as tk


import datetime
import time
import os
import shutil
import sqlite3

import GUIFileTransferAppPy35 as gui
import DBFunctionsFileTransferAppPy35 as db

   


#Function that determines a file's last modified time. The Function is called by fileMove function and passes source file as argument. 

def recentEdit(fileSource):
        
        fileAge = os.path.getmtime(fileSource) # returns time of last file modification (in seconds since epoch)
        lastTransfer = db.readDB() # returns time of last transfer (in seconds since epoch) from FileTransfer Database TIMESTAMP
        dayMarker = time.time() - 86400  # returns current time (in seconds since epoch) subtracted by a day (minus 24 hours = 86400 sec)
        if fileAge > lastTransfer:
                return True
        else:
                return False




# Function accepts two parameters: self and (i)source location 

def fileCheck(self, source): 
    
    fileCheckList = []

    gui.debugfileCheck(self, source)
    
    for files in os.listdir(source): # loop through source folder
        
        fileSource = os.path.join(source, files)
        # if the files end with '.txt' and they have been modified in the past 24 hours, as determined by calling recentEdit function
        if files.endswith('.txt') and recentEdit(fileSource):
            fileAge = os.path.getmtime(fileSource) # time of last file modification
            fileCheckList.append((files) + " - " + time.ctime(fileAge))
            print (fileCheckList)       

    return tk.messagebox.showinfo(title="Modified Files",
                                   message= "In folder: %s .\nThe following '.txt' files were modified after last transfer: \n %s" %(source, fileCheckList))




# Function accepts three parameters: self, (i)source location and (ii)destination location

def fileMove(self, source, destination):

    fileMoveList= []
    
    # gui debugger that ensures proper folder selections for file transfer.
    # debugfileMove function skips fileMove function if source/destination folders are not alternate folders or do not exist.
    while gui.debugfileMove(self, source, destination) is True:
    
            for files in os.listdir(source): # loop through source folder
                fileSource = os.path.join(source, files) 
                fileDestination = os.path.join(destination, files) # use os.path.join to create source-destination path
                # if the files end with '.txt' and they have been modified in the past 24 hours, as determined by calling recentEdit function
                if files.endswith('.txt') and recentEdit(fileSource):
                        fileAge = os.path.getmtime(fileSource) # time of last file modification
                        print ("Moving {} modified on {}.".format(files, time.ctime(fileAge)))
                        fileMoveList.append((files) + " - " + time.ctime(fileAge))
                        shutil.move(fileSource, fileDestination) # move files using the absolute path
                        print ("FILE MOVED. \tNew Directory: {}.\n".format(destination)) # print file name and destination

        # Timestamp file transfer date to the File Transfer DATABASE (transfertimestamps TABLE).
            db.FileTransfer_TIMESTAMP()
        # Update the GUI with the Last Transfer Time.     
            gui.GUILastTransfer(self)
        # Return GUI output to USER and confirm File Transfer success.
            return tk.messagebox.showinfo(title="Files Transferred!",
                                  message= "The following '.txt' files were moved: \n.%s" %(fileMoveList))

