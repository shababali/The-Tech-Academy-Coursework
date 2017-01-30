'''Python: 2.7.11

Tech Academy Python Drill - Employee Pay Program.

A simple drill to learn class based object oriented programming (OOP) concepts and play with
functions and parameters,
passing arguments,
classes,
methods and properties,
variable scope,
data types,
loops,
conditional statements,
mathematical and logical operators etc.

This program was modeled after tutorials on OOP by Corey Schafer.

It utilizes a class named Employee with properties such as name and pay and then utilizes methods to
ammend the pay property (self.pay) of Employee class instances while assigning awards.



ASSIGNMENT:
Write a program in Python 2.7 using IDLE that demonstrates the following concepts:
Use comments in your program to denote where you demonstrate each step.
If there are any concepts you are not able to demonstrate, research them online first.
If you still have trouble, ask an Instructor for assistance. 

1. Assign an integer to a variable

2. Assign a string to a variable

3. Assign a float to a variable

4. Use the print function and .format() notation to print out the variable you assigned  

5. Use each of these operators +, - , * , / , +=, ­= , %

6. Use of logical operators: and, or, not

7. Use of conditional statements: if, elif, else

8. Use of a while loop

9. Use of a for loop

10. Create a list and iterate through that list using a for loop to print each item out on a new line

11. Create a tuple and iterate through it using a for loop to print each item out on a new line

12. Define a function that returns a string variable.

13. Call the function you defined above and print the result to the shell'''




bonus = 500
# 'bonus' is a global variable that creates new Employee instances when
# the ' apply_raise ()' method (of class Employee) is called.

class Employee:

    raise_amount = 1.05
    
     
    def __init__(self, empID, first, last, pay): # __init__ takes 5 arguments as Employee class instance properties. 
        self.empID = empID
        self.first = first
        self.last = last
        self.pay = pay
        #instance variables defined within the class that are unique for each Employee instance.
        # Many of the variables in the program contain integer, string, floating point and boolean
        # data types. For this program, the boolean data types are used mainy as local variables within
        #condtion statements of functions.
    
    
# Functions defined within a class are methods.
# The following methods are utilized to generate instances of the class Employee.
# The class instances (or objects) have methods such as eMail and properties such as empID pr pay.
# Objects are essentailly the the abstracted elements in the program that share relationships to
# implement/compile logical operations.

#12. Define a function that returns a string variable.
#4. Use the print function and .format() notation to print out the variable you assigned

    def eMail(self):
        return '{}.{}@techacademy.com'.format(self.first.lower(),self.last.lower())


    def fullName(self):
        return '{} {}'.format(self.first.title(),self.last.title())

#3. Assign float value to revenue parameter of Employee class.
#   Calling employeeValue method will assign a float value to a variable.
 

    def employeeValue(self):
        return float(self.pay)
    
    def apply_raise(self): # Use of operators +, - , * , / , +=, ­= , % - avoided += and -=
        self.pay = int((self.pay * self.raise_amount) + bonus) #Use of class variable raise_amount to change any instance of raise.
        return self.pay                                        
    #Note- bonus is defined outside scope of this method so anytime bonus is changed in the script, Employee instances,
    # chiefly their respective self.pay properties will be changed.

   
#1. Assign an integer to a variable and 2. Assign a string to a variable.
# Each class instance eg emp_1 or emp_2 is one of many objects in the program.
# The emp_x objects are variables.
# ie They are variable objects and store a value to a specific location in memory. 

emp_1 = Employee(1,'Michael','Allen',7000) # self is assumed by __init__() method
emp_2 = Employee(2,'Dylan','Dykes',4000)   
emp_3 = Employee(3,'Jesse','Johnson',7000)
emp_4 = Employee(4,'Gordon','Madden',6000)
emp_5 = Employee(5,'Rick','Ramsay',9000)
emp_6 = Employee(6,'Patrick','McCrea',8000)
emp_7 = Employee(7,'Adam','Smith',7000)
emp_8 = Employee(8,'Aja','Broferrio',10000)
emp_9 = Employee(9,'Daniel','Christie',5000)
emp_10 = Employee(10,'Aaron','Frichtl',7000)



# 10 List Example - A list (data structure) is an example of a mutable object.

Employee_Instance_List = [emp_1,
                        emp_2,
                        emp_3,
                        emp_4,
                        emp_5,
                        emp_6,
                        emp_7,
                        emp_8,
                        emp_9,
                        emp_10,]


Employee_list = [emp_1.fullName(),
                emp_2.fullName(),
                emp_3.fullName(),
                emp_4.fullName(),
                emp_5.fullName(),
                emp_6.fullName(),
                emp_7.fullName(),
                emp_8.fullName(),
                emp_9.fullName(),
                emp_10.fullName(),]


Employee_pay_list = [emp_1.employeeValue(),
                    emp_2.employeeValue(),
                    emp_3.employeeValue(),
                    emp_4.employeeValue(),
                    emp_5.employeeValue(),
                    emp_6.employeeValue(),
                    emp_7.employeeValue(),
                    emp_8.employeeValue(),
                    emp_9.employeeValue(),
                    emp_10.employeeValue(),]



    
# 11 Tuple Example - A tuple (data structure) is an example of a mutable object.

Awards = ('Bronze',
          'Silver',
          'Gold',
          'Platinum')


# Start Program

def start():
    stop = True #'stop' is an example of a local variable, ie scope is defined within this function, storing Boolean data.
    while stop == True:
        choice = raw_input('Do you want to administer employee payments? y/n: ').lower()
        if choice == "y":
            print ('Employee List:')
            for counter in range (0,10): # 10. Iterate through list using a for loop.
                print 'emp_{} = {} : $ {}'.format(counter+1, Employee_list[counter], Employee_pay_list[counter])
            print('')    
            print ('Potential Awards:')
            for counter in range (0,4): # 11. Iterate through tuple using a for loop. 
                print Awards[counter]
            print('')
            program () # calls program function which is the main body of logic and coding in this Python script.
            stop = False
        elif choice == "n":
            print('Goodbye!')
            stop = False
            exit()
        else:
            print("Please enter 'y' for 'YES', 'n' for 'NO'...")
            stop = True


   
def program():
    print ("Employee Payment Routine:")
    print('')
    stop = True
    for counter in range (0,10): # Main program iterates through employess to determine pay raise, bonus and award.
        emp = Employee_Instance_List[counter]
        print '{} : $ {}'.format(Employee_list[counter], Employee_pay_list[counter])
        choice = raw_input('Would you like to raise pay or penalize pay (r/p):  ')
        if choice == 'r':
            print ('')
            bonusChange() #calls bonus change function, does not pass arguments,however bonusChange utilizes a global variable.
            emp.apply_raise() #uses apply_raise() to ammend Employee class instance pay property
            print '{} = {} : $ {}'.format(Employee_Instance_List[counter], Employee_list[counter], Employee_pay_list[counter])
            print ('')
            print 'New Pay $ {}'.format((emp).employeeValue())
            print ('')
            assignaward(Employee_Instance_List[counter]) # calls assignaward() function to assign award to Employee
            print ('')                                   # passes Employee instance as argument
        elif choice == 'p':
            print ('')
            print ('Pay not changed.')
            print 'Pay $ {}'.format((emp).employeeValue())
            print ('')
            assignaward(Employee_Instance_List[counter]) 
            print ('')
        else:
            print ('')
            print ('Error - request not computed')
            print ('')
    print('PROGRAM END')
    exit()

    
# 13. Call the function you defined above and print the result to the shell
# Employment Payment Program calls several functions: assignaward, start, bonusChange
# The 

                    # A function to change bonus for employee, this code won't actually change the bonus
def bonusChange():  # for the Employee instance because 'bonus' variable has local scope within this function.
    bonus = 500     # Making a bonus class variable and utilizing it to change Employee instances would work.
    if (bonus%1) == 0: # redundant piece of code to just show utility in using modulus to reset a variable.
        bonus = 500
        print ('')
        print ('Establish bonus amount: The default bonus is: ')
        print bonus 
    stop = True
    while stop == True: #while loop
        choice = raw_input("Would you like to increase 'i' or decrease 'd' bonus amount? \nOr keep the default bonus 's' i/d/s: ").lower()  
        if choice == "i":
            bonus += 100 # use of += mathematical operator
            print bonus
            stop = False
        elif choice == "d":
            bonus -= 100 # use of -= mathematical operator
            print bonus
            stop = False
        elif choice == "s":
            bonus = 500 
            print bonus
            stop = False
        else:
            print("Please enter 'i' for 'INCREASE', 'd' for 'DECREASE', 's' for 'SAME' ...")
            stop = True
    return bonus



# 6. Use of logical operators: and, or, not
# 7. Use of conditional statements: if, elif, else
# Note this is my first Python Assignment and Im only using the following code in the assignaward() method
# to complete the assignment fully. I wouldn't typically code in such a non-semantic fashion.

def assignaward(empInstance):
    if ((empInstance).pay < 5000) or ((empInstance).pay == 5000):
        print (empInstance).fullName() + ': Award = ' + Awards[0]
    elif ((empInstance).pay > 10000):
        print (empInstance).fullName() + ': Award = ' + Awards[3]
    elif ((empInstance).pay > 5000) and ((empInstance).pay < 7000):
        print (empInstance).fullName() + ': Award = ' + Awards[1] 
    elif not(((empInstance).pay > 5000) and ((empInstance).pay < 7000)):
        print (empInstance).fullName() + ': Award = ' + Awards[2]
    else:
        print (empInstance).fullName() + ': Award = ' + ('NO AWARD')





if __name__ == "__main__":
    start () #Interface to access pay program by calling start() function.







