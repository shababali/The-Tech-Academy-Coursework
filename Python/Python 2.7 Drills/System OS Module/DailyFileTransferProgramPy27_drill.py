
# Python Version: Python 2.7.13
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python and OS module.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.


'''Scenario: Your company's users create or edit a collection of text files throughout the day.
These text files represent data about customer orders.

Once per day, any files that are new, or that were edited within the previous 24 hours,
must be sent to the home office. To facilitate this, these new or updated files need to be copied
to a specific 'destination' folder on a computer, so that a special file transfer program can grab
them and transfer them to the home office.

The process of figuring out which files are new or recently edited, and copying them to the 'destination' folder,
is currently being done manually. This is very expensive in terms of manpower.
You have been asked to create a script that will automaate this task, saving the company a lot of money over the long term.

Guidelines:
Use Python 2.x for this drill.
You should create two folders; one to hold the files that get created or modified throughout the day,
and another to receive the folders that your script determines should be copied over daily.'''


import datetime
import time
import os
import shutil




#Function that determines a file's last modified time. The Function is called by fileMove function and passes source file as argument. 
def recentEdit(fileSource):      
        fileAge = os.path.getmtime(fileSource) # returns time of last modification in number of seconds since the epoch
        dayMarker = time.time() - 86400  # returns current time (in seconds since epoch) subtracted by a day (minus 24 hours = 86400 sec)
        if fileAge > dayMarker:
                return True
        else:
                return False



def fileMove(source, destination): # Function accepts two parameters:(i)source location and (ii)destination location
     
    for files in os.listdir(source): # loop through source folder
        fileSource = os.path.join(source, files) 
        fileDestination = os.path.join(destination, files) # use os.path.join to create source-destination path
        # if the files end with '.txt' and they have been modified in the past 24 hours, as determined by calling recentEdit function
        if files.endswith('.txt') and recentEdit(fileSource):
                fileAge = os.path.getmtime(fileSource) # time of last file modification
                print ("Moving {} modified on {}.".format(files, time.ctime(fileAge)))
                shutil.move(fileSource, fileDestination) # move files using the absolute path
                print ("FILE MOVED. \tNew Directory: {}.\n".format(destination)) # print file name and destination
                
                


def program():
    # Execcute fileMove function by inseting a desirable source and destination folder. Eg 'C:/Users/Student/Desktop/Folder-A'  
    fileMove('C:/Users/Student/Desktop/Folder-A','C:/Users/Student/Desktop/Folder-B')



if __name__ == "__main__":
    program()
