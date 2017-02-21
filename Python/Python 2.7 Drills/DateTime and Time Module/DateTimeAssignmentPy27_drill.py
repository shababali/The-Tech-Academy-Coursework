
'''
# Python Version: Python 2.7.13
#
# Author:         Shabab Ali
#
# Purpose:        To learn Python datetime class nuances and Object Oriented Programming Concepts.
#
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.

# Assignment -Scenario: The company you work for just opened two new branches. One is in New York City,
# the other in London. They need a very simple program to find out if the branches are open or
# closed based on the current time of the Headquarters here in Portland. The hours of both
# branches are 9:00AM - 9:00PM in their own time zone.
#
# What is asked of you:
#
#Create code that will use the current time of the Portland HQ to find out the time in the NYC &
#London branches, then compare that time with the branches hours to see if they are open or
#closed.
#Print out if each of the two branches are open or closed.

'''

# The program utitilzes the 'python_datetime_classes script' that realizes UTC timezones (Python datetime abstract class, tzinfo).
# 'python_datetime_classes script' script contains USTimezone and UKTimezone classes,
# which create tzinfo objects that are both UTC offset and daylight savings time aware.
# The timezone objects imported are: Eastern, Central, Mountain, Pacific, and London.
# For such processes, Python Software Foundation reccomends the pytz library which contains the global UTC system.
# datetime.utcnow() is timezone aware.
# Also, for this assignment, time module and time.tzset() methods would have been sufficient.

#Import datetime module from the Python Standard Library

from datetime import datetime, time

#Import timezone abstract class objects from an edited python module which creates regional timezone objects that are
# UTC offset and daylight savings time aware.

from datetimeoffset_module import Eastern, Central, Mountain, Pacific, London



class Branch: #Branch class that accepts 2 arguments: (i)name of branch and (ii)regional timezone abstract class objects 

    def __init__(self, branchName, timezone):  
        self.name = branchName                  # Branch class name attribute
        self.timezone = timezone 
        self.localtime = datetime.now(timezone) # Branch class datetime attribute - timezone and daylight savings aware 


     
    def status(self): #Method in Branch to determine OPEN/CLOSED status

        hourOPEN = time(9,0,0)  # Branch opens @ 9 AM or time - 9 hours
        hourCLOSE = time(21,0,0)  # Branch closes @ 9 PM or time - 21 hours
        branchTime = datetime.time(self.localtime) #creates time instance from Branch class datetime attribute self.localtime 

        if (hourOPEN <= branchTime <= hourCLOSE): # returns branch status based based on local time attribute
            return 'OPEN'
        else:
            return 'CLOSED'
        

#Instantiate the Program's Branch Objects using the Branch class.
pdx = Branch('Portland', Pacific) 
nyc = Branch('New York', Eastern)
ldn = Branch('London', London)


#Create a LIST of the Program's Branch Objects
branchesList = [ 
    pdx,
    nyc,
    ldn
    ]


# Main Program function loops through Branch Objects LIST, and prints a Branch name property and status method. 
def locationOPENCheck():
    print ("Check Location Status:""\n")
    for BranchInstance in branchesList:
        print ("{} BRANCH :-- {}".format(BranchInstance.name, BranchInstance.status()))
        print ("Local Date and Time: {}".format((BranchInstance.localtime).strftime('%Y-%m-%d  %H:%M:%S %p'))) #format datetime with strftime()
        print ("")
    
    


if __name__ == "__main__":
    locationOPENCheck()



