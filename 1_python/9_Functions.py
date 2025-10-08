"""

def hello():
	print("Hello")

hello()

"""

"""

Parameterized Functions
->If you want to give a function a default value you can use = 

"""
"""

def hello(name="Ishu"):
    print("Hello",name)

hello()
hello(input("What is Your name"))

"""
"""

this is A older version to use python the more Conventional way to write python code is
As you are defining functions at top and the logic is going down and down so to solve this we do

"""

def main():
    name=input("what is Your naame")
    hello(name)
    print(sum(2,3))
def hello(to):
    print("hello "+to)
def sum(a,b):
    return a+b

main()

# Now its printing some value what if you want to return something you can just use keyword return to do so


