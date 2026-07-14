a = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 }
b = 10
for y in a :
    print (y * b)

a = { 1 , 2 , 3 , 4 , True , 5 , 6 , 7 , 8 , 9 , "pyhton" }
b = set()
c = 0
for y in a :
    if type(y) is int :
        c += y
print (c)
      
#Given a set of strings, use a loop to count how many elements have length greater than 4.
a = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
c = 0
for y in a :
    if y > 4 :
     c +=1
print (c)       

#Write a program to filter out all odd numbers into a new set using a loop.
a = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
c = set()
for y in a :
 if y % 2 != 0 :
  c.add(y)
print (c)

#Given a list of sets, combine (union) all of them into a single set using a loop.
a = { 35 , 78 , 90 , 11 }
b = { 12 , 32 , 9 , 67 }
c = { 94 , 41 , 77 , 65}
d = set()
for x in a :
   d.add(x)
for y in b :
   d.add(y)
for z in c :
   d.add(z)         
print (d)