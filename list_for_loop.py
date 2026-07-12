# Write a program to print each element of a list on a new line using a for loop.
a = ["hello" , "world" , "jaipur" , "butterfly" , "green"]
for y in a :
    print (y)

# Write a program to find the sum of all numerical elements in a list using a loop.
a = [67 , 83 , 12 , 90 , 56]   
b = 0 
for y in a :
    b +=  y
print (b)

## Write a program to find the largest number in a list without using the built-in max() function
a = [67 , 83 , 12 , 90 , 56]   
b = []
for y in a :      
      



#Write a program to count how many times a specific element appears in a list using a loop.
a = ["hello" , "world" , "jaipur" , "butterfly" , "green" , "hello", "paris", "hello"]
b = 0
for y in a :
    if y == "hello" :
     b += 1
print (b)     

# Write a program to create a new list that contains the squares of all numbers from an existing list.
a = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
b = []
for y in a :
   b.append(y * y)
print (b)

# Write a program to reverse the elements of a list in-place using a loop.   
a = ["hello" , "world" , "jaipur" , "butterfly" , "green" , "hello", "paris"]
b = []
for y in a :
   b = a[::-1]
print (list(b))   

# Write a program to find and print only the even numbers from a list of integers.
a = [1 , 2  , 3 , 4 , 5 , 6 , 7 , 8 , 9]
b = []
for y in a :
   if y % 2 == 0 :
      print (y)  

# Write a program to remove all duplicate values from a list using a loop.
a = [1 , 2  , 3 , 4 , 5 , 6 , 7 , 8 , 9  , 6 , 5 , 1]
b = []
for y in a :
   if y not in b :
    b.append(y)
print (b)
   
