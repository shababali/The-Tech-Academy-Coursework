

# Python Version: Python 3.5.1
#
# Author:         Shabab Ali
#
# Purpose:        Assignment to learn Python, Shutil module and OS module.
#                 Function Design and integration.
#                 
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.


# The following script is a module that comprises 'BACK-END' Functions for the File Transfer Application Graphic User Interface.
# These functions link user selections to the main programs functions, and load the File Transfer Application GUI.
# The Main Program should be executed through MAINFileTransferAppPy35.py

# Modified from a FileCheck Script. 




from tkinter import*
import tkinter as tk

import datetime
import time
import os



import OSFunctionsFileTransferAppPy35 as functions
import DBFunctionsFileTransferAppPy35 as db



def load_gui(self): # Populate the master Frame with Tkinter widgets in grid geometry.

    
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
    self.button_source = tk.Button(self.master, width=10, height=2, text="Source", command=lambda: getSource(self))                            
    self.button_source.grid(row=0, column=2, padx=(20, 0), pady=(10, 20))

    # create and place a destination button
    self.button_dest = tk.Button(self.master, width=10, height=2, text="Destination", command=lambda: getDestination(self))                              
    self.button_dest.grid(row=1, column=2, padx=(20, 0), pady=(10, 20))
    
    # create and place a file check button
    self.button_transfer = tk.Button(self.master, width=15, height=2, text="File Check",
                                     command=lambda: functions.fileCheck(self, self.custom_source))                                                     
    self.button_transfer.grid(row=2, column=0, padx=(0, 0), pady=(10, 10))


    # create and place a transfer file button
    self.button_transfer = tk.Button(self.master, width=15, height=2, text="Transfer Files",
                                     command=lambda: functions.fileMove(self, self.custom_source, self.custom_dest))                                                     
    self.button_transfer.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))


    # GUI Last Transfer update function - allows calling from the File Transfer process
    # facilitating real-time GUI updates during program operation.
    GUILastTransfer(self)

    
def GUILastTransfer(self):
    # create and populate the label_print widget
    self.label_print = tk.Label(self.master, width=50, height=2, text="Last Transfer: {}".format(time.ctime(db.readDB())))
    self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

       


#center Window Function.
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





'''GUI BACK END FUNCTIONS'''


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


# debugfileCheck Function accepts parameter:
# (i)source location -
# selected by user and handles cases where a valid Source folder has not been selected.

def debugfileCheck(self, source):

    source = self.custom_source
    destination = self.custom_dest
    
    if source == destination:
        tk.messagebox.showwarning(title="Input Error", message= "Please select a unique SOURCE and DESTINATION Folder")
        
    elif not os.path.exists(source) or isinstance(source, str) is not True :
        tk.messagebox.showwarning(title="Input Error", message= "Please select a valid SOURCE Folder")
        
    else:
        return True




# debugfileMove Function accepts parameters:
# (i)source location and (ii)destination location -
# selected by user and handles cases where a valid Source and/or Destination folder has not been selected.

def debugfileMove(self, source, destination):

    source = self.custom_source
    destination = self.custom_dest
    
    if source == destination:
        tk.messagebox.showwarning(title="Input Error", message= "Please select a unique SOURCE and DESTINATION Folder")
        return False
    elif not os.path.exists(source):
        tk.messagebox.showwarning(title="Input Error", message= "Please select a valid SOURCE Folder")
        return False
    elif not os.path.exists(destination):
        tk.messagebox.showwarning(title="Input Error", message= "Please select a valid DESTINATION Folder")
        return False
    else:
        return True








