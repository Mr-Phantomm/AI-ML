"""

Make a calculator in Python 

input take 2 numbers and operation 
output answer

"""

num1=int(input("Enter first number"))
num2=int(input("Enter Second number"))
num3=input("Operation??")

if(num3[0]=="+"):
    print(num1+num2)
if(num3[0]=="-"):
    print(num1-num2)
if(num3[0]=="*"):
    print(num1*num2)
if(num3[0]=="/"):
    print(num1/num2)
