# Python: 3.6.0
# Tech Academy Python Drill - Functional Programming Script to learn Python Concepts
# Key Concepts - Variable Assignment, Expressions, Operations and Program Input/Output.  

print("Let's see how long you have lived in days, minutes and seconds.")
name = input("name:  ")
print("now enter your age")
age = int(input("age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print(name, "has been alive for", days, "days", minutes, "minutes and", seconds, "second!  Wow you are so young!")
print("{} has been alive for {} days, {} minutes, and, {} seconds! Wow you are so young!".format(name,days,minutes,seconds))
