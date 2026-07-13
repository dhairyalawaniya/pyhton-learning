#Write a program to iterate through a dictionary and print all its keys
a = { "name": "alice", "age": 29, "city": "New York" }
print (a.keys())

#Write a program to iterate through a dictionary and print all its values.
a = {"name": "alice", "age": 29, "city": "New York" }
print (a.values())

#Write a program to print both keys and values of a dictionary side-by-side using a loop.
# a = {"name": "alice", "age": 29, "city": "New York" }
# for y in a :
#    print (y.items())

#dictionary of items and their prices, write a program using a loop to calculate the total cost of ll items.
a = { 
 "apples" : 90,
 "flour" : 60,
 "bread" : 20,
 "cheese" : 50,
 "butter" : 15,
 "choclate" : 150,
 "biscuits" : 10
}
c = 0
for y in a :
    c += a[y]
print (c)

#Write a program to create a dictionary where the keys are numbers from 1 to 5 and the values are the quares of those numbers using a `while` loop.
a = {}
c = 1
while c < 6 :
   a[c] = c * c
   c += 1
print (a)

#Given a dictionary, write a program to filter out and create a new dictionary containing only the items here the value is an even number.
a = { 
 "apples" : 90,
 "flour" : 61,
 "bread" : 20,
 "cheese" : 55,
 "butter" : 15,
 "choclate" : 150,
 "biscuits" : 10
}
c = {}
b = 1
for y in a :
    if a[b] % 2 == 0 :
        