
# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python, Shutil module and OS module.
#                 Function Design and integration.
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
You have been asked to create a script that will automate this task, saving the company a lot of money over the long term.
'''

# Modified File Transfer Script to create Function Module for File Check Program/Application.
# This script provides 'BACK-END' Functions for the File Check Application.



from tkinter import*
import tkinter as tk



import datetime
import time
import os


'''Tkinter GUI BACK-END FEATURES - Functionality'''


#Gets Tkinter based user selected SOURCE folder, assigns directory to self.custom_source

def getSource(self):

    #Clears entry box, then replaces it with the selected file source path.

    self.text_source.delete(0, 50)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)

    return self.custom_source
      
#Gets Tkinter based user selected DESTINATION folder, assigns directory to self.custom_dest

def getDestination(self):

    #Clears the current entry box, then replaces it with the selected file destination path.

    self.text_dest.delete(0, 50)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)
      
    return self.custom_dest

'''FILE CHECK APPLICATION Main Program - Functionality'''


# recentEdit function that determines a file's last modified time. The Function is called by fileCheck function and passes source file as argument.

def recentEdit(fileSource):      
        fileAge = os.path.getmtime(fileSource) # returns time of last modification in number of seconds since the epoch
        dayMarker = time.time() - 86400  # returns current time (in seconds since epoch) subtracted by a day (minus 24 hours = 86400 sec)
        if fileAge > dayMarker:
                return True
        else:
                return False

# fileCheck Function accepts parameter source location - selected by user.

def fileCheck(self, source): 
    
    filecheckList = []
    debugfileCheck(self, source) # error-handling section that forces the user to select a valid folder through GUI buttons.
    
    for files in os.listdir(source): # loop through source folder
        
        fileSource = os.path.join(source, files)
        # if the files end with '.txt' and they have been modified in the past 24 hours, as determined by calling recentEdit function
        if files.endswith('.txt') and recentEdit(fileSource):
            fileAge = os.path.getmtime(fileSource) # time of last file modification
            filecheckList.append((files) + " - " + time.ctime(fileAge))
            print (filecheckList)        

    return tk.messagebox.showinfo(title="Modified Files",
                                  message= "In folder: %s. \nThe following '.txt' files were modified within 24 hours: \n %s" %(source, filecheckList))


# debugfileCheck Function accepts parameter:(i)source location - selected by user and handles cases where a valid Source folder has not been selected.

def debugfileCheck(self, source):

    source = self.custom_source
    destination = self.custom_dest

    if source == destination:
        tk.messagebox.showwarning(title="Input Error", message= "Please select an alternate SOURCE and DESTINATION Folder")
    
    elif not os.path.exists(source):
        tk.messagebox.showwarning(title="Input Error", message= "Please select a valid SOURCE Folder")

    else:
        return True        
   



