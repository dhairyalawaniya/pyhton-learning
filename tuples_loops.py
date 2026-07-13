# Write a program to iterate through a tuple and print each element on a new line.
a = ("hello" , "world" , "python" , "java" , "script")
for y in a :
    print (y)

# Write a program to find the sum of all numerical elements in a tuple using a for loop.    
a = (89 , "pyhton" , "butterfly" , 67 , 12 , 34 , 44 , 90 , 71)
b = 0
for y in a :
 if type(y) is int :
  b += y
print (b)

# Given a tuple of numbers, write a program to count how many even numbers it contains using a loop.
a = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 )
c = 0
for y in a :
 if y % 2 == 0 :
    c += 1
print (c)

# Write a program to convert a tuple of strings into a single sentence/string using a loop.
a = ("hi" , "my" , "name" , "is" , "jarvis" )
b = []
for y in a :
  b.append(y)
  c = " ".join(b)
print (c)

# Write a program to check if an element exists in a tuple using a loop (without using the in keyword).
a = ("nightmare" , "alps" , "foxtrot" , "delta" , "zico")
b = input('enter the word: ')
for y in a :
  if y == b :
   print ("yes , it exists")

#tuple of mixed data types, write a program using a loop to create a new tuple containing only the integers.
a = (89 , "pyhton" , "butterfly" , 67 , 12 , 34 , 44 , 90 , 71)
b = []
for y in a :
  if type(y) is int :
    b.append(y)
  c = tuple(b)
print (c)

#Write a program to find the largest number in a tuple without using the built-in max() function.
a = (89 , 67 , 12 , 34 , 44 , 90 , 71)
b = []
for y in a :
    b.append(y)
    b.sort()
print (b[-1])

#Given a tuple, write a program to copy its elements into a list in reverse order using a loop.
a = (89 , "pyhton" , "butterfly" , 67 , 12 , 34 , 44 , 90 , 71)
b = []
for y in a :
  b.append(y)
print (b[::-1])

#prg. find the index position of a specific element in a tuple using a loop (without using the .index() method).





#a nested tuple (e.g., ((1, 2), (3, 4))), write a program using a nested loop to print every individual number.
a = ((1, 2), (3, 4))
for y in a :
  for x in y:
    print (x)