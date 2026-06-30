#Ask the user to enter:
#A word
#A character to search for
#Using a while loop, count how many times that character appears in the word.
a = input("enter a word ")
d = input("character to search for: ")
b = len(a)
c = 0
character_count = 0
while c < b :
    if a[c] in d :
        character_count += 1
    c += 1
print (character_count)    
