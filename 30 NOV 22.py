import math
a=min(1,2,3)
b=max(1,2,3)
print(a)
print(b)
c=math.floor(2.55)
d=math.ceil(2.05)
print(c)
print(d)

#for loop
student=["Anurag","sunil","shankar"]
for i in student:
  print(i)

  for i in "anurag":
  print(i)

  for i in range(5):
  print(i) 

student = ["Anurag","sunil","shankar"]
for i in student:
  if i=="sunil":
    break
  print(i)

 student = ["1","2","3","4","5","6"]
for i in student:
  if i=="3":
    break
  print(i)

for i in range(1,6):
  print(i)

for i in range(1,20,3):
  print(i)

for i in range(20,1,-3):
  print(i)

#Nested for loop
student = ["Anurag","sunil","shankar"]
color  =["red","blue","green"]
for i in student:
  for j in color:
    print(i,j)

subjects = ["maths","science","computer"]
marks=["55","98","56"]
for i in subjects:
  for j in marks:
    print(i,j)

i=1
while i<5:
  j=2
  while j<=4:
    print(i*j)
    j=j+1
  i=i+1
  print("\n")

# Printing a pattern using nested for loop
n=int(input())
for i in range(0,n):
  for j in range(0,i+1):
    print("*", end="")
  print()

import random 
li=[] #global variable li
for i in range(0,5):
  n=random.randint(1,10)   #local varible n
  li.append(n)
print(li)
#Another datordered &atype:Tuple
#ordered & unchangeable
a=("maths","science","computer")
print(type(a))
print(len(a))
print(a)
print(a[1])

a=("maths","science","computer")
if "mahs" in a :
  print("Yes it is present") 
else:
 print("not in the a")

a=("maths","science","computer")
if "maths" in a :
  print("Yes it is present") 
else:
 print("not in the a")


#type casting
a=("maths","science","computer")
b=(list(a))
b[1]="ambi"
a= tuple(b)
print(a)

a=("maths","science","computer")
b=(1,2,3)
c=a+b
print(c)

# Another data type : set
# unordered & unchangable
a={"maths","science","computer"}
for i in a:
  print(i)

a={"maths","science","computer"}
a.add("ambi")
print(a)

a={"maths","science","computer"}
#a.add("ambi")
#print(a)
b={"1","2","3"}
c=a.union(b)
print(c)

#ordered changeable
#anathor data type dictonary
a={
    "name":"anurag",
   "company":"cipherschools",
   "colledge":"Institute of internet"
}
print(a)


a={
    "name":"anurag",
   "company":"cipherschools",
   "colledge":"Institute of internet"
}
print(a["name"])

#print(a)
#print(a["name"])
a["degree"]="Engineering"
#print(a)
#print(a.key())
if "name"in a:
  print("yes it exist")


