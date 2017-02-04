# Python: 2.7.11
# Tech Academy Python Drill - Video Tutorial by Daniel Christie
# https://www.youtube.com/watch?v=RliPr9V8f6A&feature=youtu.be - 2017/01/20.

# Purpose: To learn:
# Passing Arguments through Functions and returning Values.
# Variable scope and closure.




#get user name 'string' data type:


def start (nice=0,mean=0,name=""):
    #get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    '''
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    '''
    if name != "": # meaning, if we do not already have this user's name, then they are a new player and we need to get their name
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                    print("At the end of the game your fate will be influenced from your actions.")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    print ("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 5: # if condition is True, call win() function passing in the (nice,mean,name) arguments
        win(nice,mean,name)
    if mean > 5: # if condition is True, call mean() function passing in the(nice,mean,name) arguments
        lose(nice,mean,name)
    else: # else, call nice_mean() function passing in the (nice,mean,name) arguments
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you now live in a palace!".format(name))
                                # Substitute the {} wildcards with the correct variables. 
    again(nice,mean,name)# call again function and pass the (nice,mean,name) arguments.



def lose(nice,mean,name):
    print("\nToo bad, game over! \n{}, you live in a van by the river, wretched and alone!".format(name))
                                # Substitute the {} wildcards with the correct variables. 
    again(nice,mean,name)# call again function and pass the (nice,mean,name) arguments.



def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you later alligator!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)



    
        
if __name__ == "__main__":
    start ()


''' PRELIMINARY WARMUP: BASIC FUNCTION DESIGN - 

# integer practise:

def start ():
    print(get_number())

def get_number ():
    number = 12
    return number

if __name__ == "__main__":
    start ()


    
#get user name 'string' data type:
    #Learn importance of placeholder {} 

def start():
    print(get_name())

def start():
    print("Hello {}".format(get_name()))
    
def get_name():
    name = raw_input ("What is your name?")
    return name

if __name__ == "__main__":
    start ()



#get user name 'string' data type: 


def start ():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female" 
    get_info(f_name,l_name,age,gender)

def get_info (f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))
    
if __name__ == "__main__":
    start ()
'''
