'''
# Python Version: Python 2.7.13
#
# Author:         Shabab Ali
#
# Purpose:        To learn Python datetime class nuances and Object Oriented Programming Concepts.
#
# Tested OS:      Code written and tested to work with Windows 7 Service Pack 1.'''


# Classes and abstract classes for datetime module in Python.
# Datetime objects are typically deficient in timezone awareness and UTC awareness. Datetime objects can be made timezone aware through instantiating
# abstract classes as observed in the following implementation provided by the Python Software Foundation.
# The code has some minodewr adjustments for the drill, AND HAS SOME NOTED BUGS, at the
# daylights savings time junctions. 

# Note: Python Software Foundation actually reccomends using the pytz module for
# UTC and daylight savings times offsets.


# An implementation of current DST rules for major US and UK time zones.
# Sourced from 'Python Software Foundation'.


from datetime import tzinfo, timedelta, datetime

ZERO = timedelta(0)
HOUR = timedelta(hours=1)




def first_sunday_on_or_after(dt): # function passes a datetime object as argument to # get number of days till next Sunday.
    days_to_go = 6 - dt.weekday() # # ie 6 as per .weekday() method from the datetime module.
    if days_to_go:
        dt += timedelta(days_to_go) # adds 'days till next Sunday' to the argument datetime object.
    return dt


# In the US, since 2007, DST starts at 2am (standard time) on the second
# Sunday in March, which is the first Sunday on or after Mar 8.
# DSTSTART_2007 = datetime(1, 3, 8, 2)
# and ends at 2am (DST time; 1am standard time) on the first Sunday of Nov.
# DSTEND_2007 = datetime(1, 11, 1, 1)


class USTimeZone(tzinfo):

    def __init__(self, hours, reprname, stdname, dstname):
        self.stdoffset = timedelta(hours=hours)
        self.reprname = reprname
        self.stdname = stdname
        self.dstname = dstname

    def __repr__(self):
        return self.reprname

    def tzname(self, dt):
        if self.dst(dt):
            return self.dstname
        else:
            return self.stdname

    def utcoffset(self, dt):
        return self.stdoffset + self.dst(dt)

    def dst(self, dt):
        if dt is None or dt.tzinfo is None:
            # An exception may be sensible here, in one or both cases.
            # It depends on how you want to treat them.  The default
            # fromutc() implementation (called by the default astimezone()
            # implementation) passes a datetime with dt.tzinfo is self.
            return ZERO
        assert dt.tzinfo is self

        # In US, DST starts at 2am (standard time) on the second Sunday of March.
        dststart = datetime(1, 3, 8, 2)
        # and ends at 2am (DST time; 1am standard time) on the first Sunday of Nov.
        dstend = datetime(1, 11, 1, 1)

        start = first_sunday_on_or_after(dststart.replace(year=dt.year))
        end = first_sunday_on_or_after(dstend.replace(year=dt.year))

        # Can't compare naive to aware objects, so strip the timezone from
        # dt first.
        if start <= dt.replace(tzinfo=None) < end:
            return HOUR
        else:
            return ZERO

# In the UK, DST starts at 2am (standard time) on the last
# Sunday in March, which is the first Sunday on or after Mar 25.
# UKDSTSTART_2007 = datetime(1, 3, 25, 2)
# and ends at 1am (DST time; 1am standard time) on the last Sunday of Oct.
# UKDSTEND_2007 = datetime(1, 10, 26, 1)

class UKTimeZone(tzinfo):

    def __init__(self, hours, reprname, stdname, dstname):
        self.stdoffset = timedelta(hours=hours)
        self.reprname = reprname
        self.stdname = stdname
        self.dstname = dstname

    def __repr__(self):
        return self.reprname

    def tzname(self, dt):
        if self.dst(dt):
            return self.dstname
        else:
            return self.stdname

    def utcoffset(self, dt):
        return self.stdoffset + self.dst(dt)

    def dst(self, dt):
        if dt is None or dt.tzinfo is None:
            # An exception may be sensible here, in one or both cases.
            # It depends on how you want to treat them.  The default
            # fromutc() implementation (called by the default astimezone()
            # implementation) passes a datetime with dt.tzinfo is self.
            return ZERO
        assert dt.tzinfo is self

        # In UK, DST starts at 2am (standard time) on the last Sunday in March.
        dststart = datetime(1, 3, 25, 2)
        
        # and ends at 2am (DST time; 1am standard time) on the last Sunday of Oct.
        dstend = datetime(1, 10, 26, 1)

        start = first_sunday_on_or_after(dststart.replace(year=dt.year))
        end = first_sunday_on_or_after(dstend.replace(year=dt.year))

        # Can't compare naive to aware objects, so strip the timezone from
        # dt first.
        if start <= dt.replace(tzinfo=None) < end:
            return HOUR
        else:
            return ZERO

Eastern  = USTimeZone(-5, "Eastern",  "EST", "EDT")
Central  = USTimeZone(-6, "Central",  "CST", "CDT")
Mountain = USTimeZone(-7, "Mountain", "MST", "MDT")
Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")

London = UKTimeZone(0, "UK", "GMT", "BST")



