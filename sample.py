# python setup 
#download python environment from python.org 
#download vs code
#install the python debugger extension which is built by microsoft 



print("hello world") #1st program 

print("single line comment")

##multi line comment denoted ''' ''' and """"  """"
"""print("hello")
print("world")"""

#variable - container to store data,dynamic datatyped
#Rules - dont start with no. or symbols and start with alphabet/underscore and even case sensitive
 
# _a = 10
# print(_a)
# print(id(_a)) #prints memory location
# print(type(_a)) #type of datatype used

# a=b=c=1
# print(a,b,c)

#datatype - classifies the type of variable 
#int,float,bool,string(single/double/triple quotes),complex
#list[],tuple(),set{},dictionary{}
#frozenset,

#str methods -lower(),upper,endsWith,len,startswith,replace,split,removeprefix,removesuffix,
#index,find,count(char repeat count),strip(removes spaces in str),lstrip(removes space in left side),rstrip(//lar to lstrip)

# name ="sai nath"
#print(name.replace("nath","ms"))
#print(name.split()) //['sai', 'nath'] splits into list
#print(name.removeprefix("sai")) //nath same but opp to suffix
# print(len(name)) //8
# print(name.index("s")) //0
# print(name.find("g")) #//-1 it doesn't throw error rather prints -1 if no char is present

#list [] - mutable,allow duplicates,indexing,diff types of data  
#Methods - append,extend,remove,pop,count,index,insert
# forward index - 0 to size-1
# negative index - -1 to size

# slice - [start:stop:skip]

lstSam = [1,1.2,"sai",False,1]
# print(lstSam[2]) //sai
# print(lstSam[-2]) //sai
# print(lstSam[0:2:1]) //[1, 1.2] slice
# lstSam.append("nath") //[1, 1.2, 'sai', False, 'nath'] 
# print(lstSam) //[1, 1.2, 'sai', False, 'nath']  adds at end 
# lstSam.extend("ms")
# print(lstSam) //[1, 1.2, 'sai', False, 'm', 's'] adds list at end 
# lstSam.extend([5,7])
# print(lstSam)//[1, 1.2, 'sai', False, 5, 7]
# print(lstSam.count(1)) //2 prints count of repeated element in list
# lstSam.remove("sai")
# print(lstSam) //[1, 1.2, False, 1]
# .pop(index no)
# .index(element)
# .insert(index,element)

#tuple()- immutable,diff type,indexng and slicing,duplicates
# no append,can't modify element
# concatination,iteration,membership operators(in,notin),identity(is,isnot),repetation

tupSam = (1,1.2,"sai",False,1)
# print(type(tupSam))
# print(tupSam[2]) //sai
# print(tupSam[-3]) //sai
# slice as list
# print(min(tupSam)) //prints min value when int values are in tuple
#max(tupsam),sum(tupsam),len(tupsam)
t1 =(1,2)
t2 =(3,4)
# print(t1+t2) //(1, 2, 3, 4) concatinate
# print(t1*2) //(1, 2, 1, 2) repeats the tuple and append it to same tuple variable
# for i in t1:
#     print(i) // 1   2 
# print(2 in t1) //true
# print(12 not in t1) //true
#  is- print(t1 is t2) // false  true(if same elements in both tuples)
# is not-true(if no same elements in both tuples)

#dictionary{}- key value,key -immutable,value - mutable,no slicing,keys - unique,key - index
# methods- get(),update(),values(),keys(),items()

d1 = {"a":1,5.1:"sai"}
# print(type(d1))
# print(d1["a"]) //1
# print(d1.keys()) //dict_keys(['a', 5.1])
# print(d1.values()) //dict_values([1, 'sai'])
# print(d1.get(5.1)) //sai
# print(d1.items()) //dict_items([('a', 1), (5.1, 'sai')])
# print(d1.clear()) //clears items
# d1.update({True:False})
# print(d1) //{'a': 1, 5.1: 'sai', True: False} appends the item at last
# for i in d1:
#     print(i) //a   5.1 - only keys 
# for i in d1.keys():
#     print(i) //a   5.1 - only keys
# for i in d1.values():
#     print(i)  //1    sai //values
# for i,j in d1.items():
#     print(i,j) //a 1   5.1 sai

#set{}-unique,unordered,unindexed,don't allow mutable types as elements
# operations-union(),intersection,difference,is subset,is superset
#methods -add(),update,pop,remove

s1 = {1,2,"sai",2}
# print(type(s1))
# print(s1) //{1, 2, 'sai'}
# s1.add(7.7)
# print(s1) //{1, 2, 'sai', 7.7}
# s1.update({2.0,True,9.0,"ms"})
# print(s1) //{'sai', 1, 2, 9.0, 'ms'}
#.pop()  random removal of element 
#.remove(ele)
#s1.unionset(s2) - s+s2
#s1.intersection(s2) - same 
#s1.differece(s2) - returns difference from both sets that too left side set
#s2.issubset(s1) - returns true/false if all elements in s2 = s1
#s1.issuperset(s2) - returns true/false if any elements in s1 = s2

# frozenset-mutable data type to immutable data type,compulsory >1 item
# f = frozenset()
# print(type(f)) //<class 'frozenset'>
# f= frozenset(lstSam)
# print(f) //frozenset({False, 1, 'sai', 1.2}) 

# conditional
# if cond:
#     stmt
# elif cond:
#     stmt
# else:
#     stmt

#looping
# for,while
# a=1
# while a<3:
#     print("ms") //2 times
#     a+=1 
# for i in "sai":
#     print(i) // s  a  i line by line
# for i in range(0,3):
#     for j in range(0,2):
#         print(i+j) //0 1 1 2 2 3

# jumping
# pass-ignore,continue-skip,break-exit

# function-block of code
# def funcname():{
#     # logic
# }
# to import functions in another file 
# import filename(no extension)
# filename.function

#procedural oriented programming
# pgm / into functions
# top down approach
#no access specifiers
#no data security
#no overloading concept
# ex-c,pascal

# oop
# pgm / into obj
# bottom up
# access spec
# data sec
# function,operator  overloading,method overriding
# ex-c++,java,python

#class - blueprint to create obj
#class classname():
#functions = methods 
#variable = attributes/members

class Student():
    name = "ms"
    rollNo = 151
    age = 27
    def greet(self):    #self = current object,explicit
        print("hello" + " " + self.name)
    def greet(self,strName):
        self.name = strName    
        print("hello" + " " + self.name)

class Person:
    def set_name(self, name):
        self.name = name   # stored in THIS object

    def greet(self):
        print("Hello", self.name)

# p1 = Person()
# p2 = Person()

# p1.set_name("Sainath")
# p2.set_name("Rahul")

# p1.greet()  # Hello Sainath
# p2.greet()  # Hello Rahul

#not working 
    # def greet(strName):
        # print("hello" + " " + strName)

student = Student() #obj creation
# print(type(student))
# print(student.name, student.age) //ms 27
# print(student.greet()) //hello ms that too if commented below same method orelse error
# print(student.greet("sai")) //hello sai 

#inheritance = allows us to define a class that inherits all properties from parent/super/base class
# child = derived class
#single = parent -> child
#multilevel = p1 -> p2 -> c
#multiple = p1 + p2 -> c
#hierarical = p -> c1 , p -> c2 same parent to multiple child classes

#single
class Parent():
    def printP(self):
        print("parent class")
class Child(Parent):
    def printC(self):
        print("child class")

child = Child()
# child.printP()
# child.printC()

# MUltiple representation
# Class Child(fatherClass,Motherclass): 

#encapsulation - wrapping of data members and mmethos in a single unit
#access spec - public(default),private(__ double underscore),protected(_ single underscore)
#Data abstraction - hiding some part of logic to the user 

class accessSpec():
    def __init__(self,bankName,accNo):
        self._bankName = bankName
        self.__accNo = accNo
class Inherit(accessSpec):
    def printBank(self):
        print(self._bankName)

inherit = Inherit("sbi",124)
# inherit.printBank()

#Polymorphism - many forms method overriding 

# def add(a,b):
    # print(a+b)
# add(2,3) #5
# add("sai","nath") #sainath
# add([1,2],[3,4]) #[1, 2, 3, 4]

#file handing - working with various types of files on the filesystem
#read,write,append 
#files- text(plain text(readable)),binary(binary format,not readable)
#methods - open(),read(),write,close
#modes - r: - read ,w: write, a: append 

# file = open('sample.txt',mode="w") #write
# file.write("file sample")
# file.close()

# file = open('sample.txt',mode="a") #append
# file.write("for python")
# file.close()

# file = open('sample.txt',mode="r") #read
# print(file.read())
# file.close()

#exception handling - disturbing the execution of code = error/exception
#try - lets you test the block of code
#except -lets you to handle the error
# else - lets you execute the code when no error
# finally-lets you execute code irrespective of o/p  try and except block

# try:
#     logic
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("custom")











