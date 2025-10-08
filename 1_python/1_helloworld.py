
"""
Parameters are of two types:- named parameters and positional parameters
1. Positional Parameters :- these are the parameters that are according to positional like comma separated in print
2. Named Parameters :- These are the parameters that are according to corresponding names that are passed with them

"""

x = input("What your name ")
print("Hello from ",x,end='???',sep='??')

"""

Fstring : A new Feacture of python where we can use variable in a String using {}

"""

print(f"The name you took {x}")


"""

String Functions :-
1. strip() => Remove white spaces from start and End
2. capitalize() => Makes the String First character to manipulate
3. title() => Makes every First character to uppercase
"""

x="     string to manipulate   "
print(x.strip().capitalize())
print(x.strip().title())

"""

If you to change any Globally declared variable in any function you should use Global keyword

"""

x="Arun"

def myFun():
    global x
    x="Ishu"

myFun()
print("Changed x from Arun to",x);

"""

ramdom : python doesnot have any random number generation function so there is a random module to generate random numbers

"""
import random
print(random.randrange(1,10))
