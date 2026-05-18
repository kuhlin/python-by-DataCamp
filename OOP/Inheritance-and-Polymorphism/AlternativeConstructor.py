""" Context:
Python allows you to define class methods as well, using the @classmethod decorator and a special first argument cls. 
The main use of class methods is defining methods that return an instance of the class, but aren't using the same code as __init__().

For example, you are developing a time series package and want to define your own class for working with dates, BetterDate. 
The attributes of the class will be year, month, and day. You want to have a constructor that creates BetterDate objects 
given the values for year, month, and day, but you also want to be able to create BetterDate objects from strings like 2020-04-30.

You might find the following functions useful:

.split("-") method will split a string at"-" into an array, e.g. "2020-04-30".split("-") returns ["2020", "04", "30"],
int() will convert a string into a number, e.g. int("2019") is 2019 .

Note: For each step, at the end of the class add a multiline comments explaining your solution
"""

import datetime

# Instructions: 

""" Step 1:
Add a class method from_str() that:

- accepts a string datestr of the format'YYYY-MM-DD',
- splits datestr and converts each part into an integer,
- returns an instance of the class with the attributes set to the values extracted from datestr.
"""

""" Step 2:
For compatibility, you also want to be able to convert a datetime object into a BetterDate object.

Add a class method from_datetime() that accepts a datetime object as the argument, and uses its 
attributes .year, .month and .day to create a BetterDate object with the same attribute values
"""

class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
    """
    Explanation for Step 1:
    The from_str class method takes a date string in 'YYYY-MM-DD' format, splits it into parts,
    converts each part to an integer, and returns a new instance of BetterDate using cls(year, month, day).
    This allows creating BetterDate objects from strings without using the __init__ method directly.
    """
    
    # Define a class method from_datetime
    @classmethod
    def from_datetime(cls, datetime_obj):
        # Extract year, month, day from the datetime object
        year = datetime_obj.year
        month = datetime_obj.month
        day = datetime_obj.day
        # Return the class instance
        return cls(year, month, day)
        
    """
    Explanation for Step 2:
    The from_datetime class method takes a datetime object, extracts its year, month, and day attributes,
    and returns a new instance of BetterDate with those values. This provides compatibility for converting
    datetime objects to BetterDate objects.
    """
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

# Test from_datetime
dt = datetime.datetime(2020, 4, 30)
bd2 = BetterDate.from_datetime(dt)
print(bd2.year)
print(bd2.month)
print(bd2.day)