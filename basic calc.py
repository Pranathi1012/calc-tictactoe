# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:40:11 2021

@author: Pranathi
"""

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=int(input("Select operation from 1,2,3,4 : "))

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice==3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice==4:
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")