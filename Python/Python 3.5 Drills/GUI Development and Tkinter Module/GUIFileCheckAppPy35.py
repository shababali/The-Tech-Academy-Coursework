
# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python, GUI design and tkinter module. Fashioned in mold of Daniel Christie's phonebook.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.

'''Scenario: You recently created a script that will check a folder for new or modified files,
and then copy those new or modified files to another location.
Users are asking for a user interface to make using the script easier and more versatile.
Desired features of the UI:
 Allow the user to browse to and choose a specific folder that will contain the
files to be checked daily.
 Allow the user to browse to and choose a specific folder that will receive the
copied files.
 Allow the user to manually initiate the 'file check' process that is performed by
the script.

Note - Model function script from Python 2.7 Daily File Transfer.
'''


from tkinter import*
import tkinter as tk

import datetime
import time
import os

import FunctionsFileCheckAppPy35 as functions



# Main Application Graphic User Interface:

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define max and min size of frame
        self.master = master
        self.master.minsize(450, 200)
        self.master.maxsize(450, 200)

        # This CenterWindow method will center our app on the user's screen
        center_window(self,500,300)

        # give the master frame a name
        self.master.title("Daily File Transfer Application")

        # give background color
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master


        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free. For example: 'insert file name'.load_gui(self)
        # This module contains all GUI functions, because the application is relatively small.
        load_gui(self)

        
# Populate the master Frame with Tkinter widgets in grid geometry.

def load_gui(self): 

    
    # create an entry text box for source button
    self.custom_source = StringVar()
    
    # set text box to a default string
    self.custom_source.set('Select SOURCE Directory')

    # set the width to 50 characters, background colour offsett and display directory source
    self.text_source = tk.Entry(self.master, width=50, bg="#FFFFFF", textvariable=self.custom_source)
    self.text_source.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(10, 0), pady=(10, 20))

    # create an entry text box for destination button
    self.custom_dest = StringVar()

    # set text box to a default string
    self.custom_dest.set('Select DESTINATION Directory')

    # set the width to 50 characters, background colour offsett and display directory destination
    self.text_dest = tk.Entry(self.master, width=50, bg="#FFFFFF", textvariable=self.custom_dest)
    self.text_dest.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(10, 0), pady=(10, 20))

    # create and place a source button
    self.button_source = tk.Button(self.master, width=10, height=2, text="Source", command=lambda: functions.getSource(self))                            
    self.button_source.grid(row=0, column=2, padx=(20, 0), pady=(10, 20))

    # create and place a destination button
    self.button_dest = tk.Button(self.master, width=10, height=2, text="Destination", command=lambda: functions.getDestination(self))                              
    self.button_dest.grid(row=1, column=2, padx=(20, 0), pady=(10, 20))
    
    # create and place a file check button
    self.button_transfer = tk.Button(self.master, width=15, height=1, text="File Check",
                                     command=lambda: functions.fileCheck(self, self.custom_source))                                                     
    self.button_transfer.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))



#center ParentWindow Function.
    
def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)




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
