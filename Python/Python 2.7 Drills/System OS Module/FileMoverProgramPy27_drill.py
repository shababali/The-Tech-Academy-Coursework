# Python Version: Python 2.7.13
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python, Shutil module and OS module.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.

'''Scenario: Your employer wants a program to move all his .txt files from one folder to another
with the click of a button. On your desktop make 2 new folders. Call one Folder A &
the second Folder B. Create 4 random .txt files & put them in Folder A.

Plan:
- Move the files from Folder A to Folder B.
- Print out each file path that got moved onto the shell.
- Upon viewing Folder A after the execution, the moved files should not be there.'''


import shutil
import os


def fileMove(source, destination): # Function accepts two parameters:(i)source location and (ii)destination location.
     
    for files in os.listdir(source): # loop through source folder.
        fileSource = os.path.join(source, files) 
        fileDestination = os.path.join(destination, files) # use os.path.join to create source-destination path.
        if files.endswith('.txt'): # if the files end with .txt, move them and print that it occurred.       
            shutil.move(fileSource, fileDestination) # move the files using the absolute path.
            print("Moved {} to {}.".format(files, destination))# print filename and destination that file was moved to.


def program():
    fileMove('C://Users//Student//Desktop//Folder-A', 'C:/Users//Student//Desktop//Folder-B')


if __name__ == "__main__":
    program()
