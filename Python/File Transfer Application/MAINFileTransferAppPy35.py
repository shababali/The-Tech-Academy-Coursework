
# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Use Python, Tkinter library (Python GUI) and Python modules to build a file transferring application with database
#                 mediated tracking utility.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.

'''
Scenario: You recently created a script that will check a folder for new or modified files, and then
copy those new or modified files to another location. You also created a UI that makes using the script
easier and more versatile.
Users are reporting issues with the current system you've made. Specifically, they are having to manually
initiate the 'file check' script at the same time each day. Because they aren't doing this at the EXACT
same time each day, some files that were edited right around the time the script was meant to be run were
missed, and weren't copied to the outgoing files destination.
This means you will have to provide for recording the last time the 'file check' process was performed,
so that you can be sure to cover the entire time period in which new or edited files could occur.
To do this, you will need to create a database with a table that can store the date and time of the last 'file
check' process. That way, you can use that date/time as a reference point in terms of finding new or
modified files.
As part of this project, the users are asking that their UI display the date and time of the last 'file check'
process.
You have been asked to implement this functionality. This means that you will need to
• create a database and a table
• modify your script to both record date/time of 'file check' runs and to retrieve that data for use in
the 'file check' process, and
• modify the UI to display the last 'file check' date/time
'''


from tkinter import*
import tkinter as tk


import datetime
import time
import sqlite3


import GUIFileTransferAppPy35 as gui
import DBFunctionsFileTransferAppPy35 as db
import OSFunctionsFileTransferAppPy35 as functions


'''Tkinter GUI FRONT-END FEATURES'''



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define max and min size of frame
        self.master = master
        self.master.minsize(450, 270)
        self.master.maxsize(450, 270)

        # This CenterWindow method will center our app on the user's screen
        gui.center_window(self,500,300)

        # give the master frame a name
        self.master.title("Daily File Transfer Application")

        # give background color
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: gui.ask_quit(self))
        arg = self.master

        #Create a File Transfer Application Database and transfertimestamps Table
        db.createDB()
        
        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free. For example: 'insert file name'.load_gui(self)
        # This module contains all GUI functions, because the application is relatively small.
        

        gui.load_gui(self)



        


            
             




"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
