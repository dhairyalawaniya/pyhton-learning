#Ask the user to enter a sentence.
#Using a while loop, count how many vowels (a, e, i, o, u) are present in the sentence.
#Display the total number of vowels.
a = input("enter a sentence ")
c = len(a)
b = 0
vowel_count = 0
while b < c:
    if a[b] in aeiouAEIOU  :
      vowel_count += 1
    b += 1

print (vowel_count)      

     