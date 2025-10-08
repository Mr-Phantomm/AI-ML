"""

List are used to store multiple items in a single variable
Lists are ordered, Changeable and allow duplicate values
They can be transversed by their indexes
If you ADD new item in the list it will be placed at the end of the list


"""

mylist =["Apple","banana","cherry","apple","cherry"]
print(mylist)

"""

length of list is given by len(list)


"""
print(f"Length of the list is {len(mylist)}")


"""

List can contain same type of variable and can also contains different type of variables

"""

mylist=["Apple",1,True,1j,1.2]

print(mylist)

"""

In the perspective of python lists are objects of type 'list' 
--->>>>  <class 'list'>

"""

print(f"Type of list is {type(list)}")

"""

You can use Constructors too  to make lists

"""
mylist=list(("apple",1,2,3))
print(mylist)


"""

To access items in list we should use index 
it uses 0 based indexing
and also negative indexing like -1 for last item and -2 for second last item 

"""

mylist = ["Arun","Garg","is","best"]
print(mylist[0],mylist[-2],mylist[-1])

"""

Range of Index /slicing : You can specify starting and ending index where to start and where to end it will return the list with specified items
list[start:end]-->>end will not be included

if you leave any value empty either start or end it will take default values as 0 or len(list) respectively

"""

myNewList=mylist[0:2]
print(myNewList)
print(mylist[:2])
print(mylist[2:])

"""

Check if list is present in the list by using in

"""

print("Arun"  in mylist)
