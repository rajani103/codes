# # # # repeated code in python
# # # grp of related code

# # built in -- int,float,eval,input(), min, max,type,len,range,round
# # modules -- a file containing functions and variables defined in seperated file -- math,random,string
# # user defined -- 

#modules
# import math
# # print(math.pi)  
# print(dir(math))  


# import math as m
# print(m.lgamma(34))  

# from math import sin
# from math import *
# print(sin(3.14))
# print(pi)

# import numpy as np 
# from numpy import trunc
# print (trunc(23))
# # print(dir(np))

# print(np.__version__)  

#user defien sfunction

# def greet():
#     print('gm,raj')
    
# greet()

# def sum():
#     print("the sum is :")
    
# sum()
# sum()

# sum()

#calling the functions

# def greet():
#     name = input("add ur name:")
#     print("hello good morning :", name)
    
# greet()


# def call(name, food):
#     print ("gm", name)
#     print ("please ete ur : " , food)
    
# call('pinky','pasta')

# def call(name, food='pasta'):
#     print ("gm", name)
#     print ("please ete ur : " , food)
    
# call('pinky')

# def sumoflist(a):
#     print("adding :")
#     sum1 = sum(a)
#     return sum1
   
# marks = [2,4,5,8]    
# sumofmarks = sumoflist(marks)
# print("sum of marks ", sumofmarks)

def greet(a):
    for i in a:
        print ("hello" , i)
        
names = ['ram','peep']
greet(names)