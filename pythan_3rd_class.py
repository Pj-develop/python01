# -*- coding: utf-8 -*-
"""PYTHAN 3RD CLASS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PwnVOpINu0jb4j1N4jH4xhNCZsezK1hO
"""

# (a+b)2=a2+b2+2ab
a = 10
b =20
sol=(a**2) + (b**2)  + 2*(a*b)
print(sol)

a = 10
b =20
sol= a*(a+b) +b*(a+b)
print(sol)

a = 10
b =20
sol=(a+b)**2
print(sol)

a = 10
b =20
sol=pow(a,2)+pow(b,2) +2*a*b
print(sol)

#importing some values
x,y,z="shlok","rohit","shikhar"
print(x)
print(y)
print(z)

a ="shlok agarwal"
print(a.upper())



#else condition=1
a = 20
b =10
if b>a:
  print("b is greater")
else:
   print("a is greater")

a = 20
b =10
if b > a:
    print("b is greater")
elif b < a:
   print("a is greater")
else:
   print("both are equal")

a = 10
b = 20
if b > a:
    print("b is greater")
elif b < a:
   print("a is greater")
else:
   print("both are equal")

a = 20
b = 20
if b > a:
    print("b is greater")
elif b < a:
   print("a is greater")
else:
   print("both are equal")

a=50
if a<60:
  print("YOUR GRADE IS C")
elif a>=60 and a<=70:
  print("YOUR GRADE IS B")
elif a>=70 and a<=80:
  print("YOUR GRADE IS B+")
elif a>=80 and a<=90:
  print("YOUR GRADE IS A")
elif a>=90 and a<=100:
  print ("YOUR GRADE IS A+")
else:
  print("FAILED")

a=int(input("ENTER YOURS MARKS"))
if a<60:
  print("YOUR GRADE IS C")
elif a>=60 and a<=70:
  print("YOUR GRADE IS B")
elif a>=70 and a<=80:
  print("YOUR GRADE IS B+")
elif a>=80 and a<=90:
  print("YOUR GRADE IS A")
elif a>=90 and a<=100:
  print ("YOUR GRADE IS A+")
else:
  print("FAILED")

import random
print(random.random())

import random
print(random.randint(1,5))

a="""hi my name is shlok
 and i am at the 
 lpu learning python as a student"""
print(a)

a="hi my name is shlok and i am at the lpu learning python as a student"
print(a)

#string operations
#slicing
b="cipherschools"
print(b[2:6])
print(b[-6:-2])

a="cipher"
b="schools"
print(a)
print(b)
print(a +" "+b)

a= "Cipherschools"
b="SHLOK"
print(a.upper())
print(b.lower())

age=16
sent="My name is somthing and my age is {}"
print(sent.format(age))

#list
col=["RAHUL","RAJ","10"]
print(col)
print(type(col))
# Learn the class list

#list
col=["RAHUL","RAJ","10"]
print(col[1:2])
print(type(col))
# Learn the class list

