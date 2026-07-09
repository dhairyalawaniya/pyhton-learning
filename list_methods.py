# How do you access and print the very last element of a list?
a = [ "hello" , True , 578 , 845.9]
print (a[-1])

# How do you reverse a list without using a loop or the .reverse() method?
a = [ 748 , 98 , "dhairya" , "apple"]
print (a[::-1])

# Write a program to add a new element to the end of an existing list.
a = ["apple" , "banana" , "cat"]
a.append("dog")
print (a)

# How do you find the total number of elements inside a list?
a = [ "hello" , "world" , "python" , "java" , 15]
b = len(a)
print (b)

# Given a list of numbers, how do you find the sum of all the items without using a loop?
a = [67 , 84 , 12 , 90 , 34 , 45]
b = sum(a)
print (b)

# How do you find the largest and smallest numbers in a list using Python's built-in functions?
a = [67 , 84 , 12 , 90 , 34 , 45]
b = max(a)
c = min(a)
print (b,c)

# How do you count how many times the number 5 appears in a list?
a = [67 , 5 ,  84 , 12 , 90 , 5 , 34 , 45]
print(a.count(5))

# Given a list, how do you extract a new list containing only the first three elements?
a = [67 , 84 , 12 , 90 , 34 , 45]
print (a[:3])

# How do you completely empty a list so that it has no elements left?
a = [67 , 84 , 12 , 90 , 34 , 45 ]
a.clear()
print (a)

#How do you check if the word "Python" exists inside a list without using any loops
a = [67 , 84 , 12 , 90 , 34 , 45 , "python"]
if "python" in a : 
 print ("yes, it is present")

