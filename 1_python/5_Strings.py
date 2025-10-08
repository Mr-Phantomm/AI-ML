"""

String in python can be surrounded by single quotation or double quotation mark

'hello' is same as "hello"

How to use "" in print Statements 2 ways --> 
1. use '' outside 
2. use /

"""

print('This is how you use \'\' and ""')


"""
Now to make multiline String we do same as we do in Multiline comments
"""

print("""Arun
is
Great
""")

"""

Strings are like Arrays of unicode characters
In python there is no such things as character it is a 1 length string
Square Brackets are used to access the character in string
==> String[x] ==> x is index

For iterating you can use loop 

"""

for x in "IshitaArunkiBachi":
    print(x,end=" ")


"""

To get the length of the string :- len(string)

"""

print(len("Arun is best"))


"""

Check whether we have some part in the string or not

"""
print(("hi") in "hi my name is Arun")
print(("hi") not in "Hi my name is ARUN");


"""

Slicing a String [start:end]
end not included

"""

string="Bachikonhmeri???"

"""

.strip() its like trim() remove the space from start and last

"""

name="    Arun     "
print(name.strip())


"""

capitalize makes the first letter of the string to uppercase

"""

name = "arun"
print(name.capitalize())


"""

But if you want every letter after space with it to get uppercase you should title()

"""

name = "arun garg"
print(name.title())


"""

You can chain the functions 

"""

name = "     arun garg     "
print(name.strip().title())

"""

Split the string according to any delimeter

"""

name ="Arun Garg"

first,last=name.split(" ")

print("First name is "+first+" Last Name is "+last)



