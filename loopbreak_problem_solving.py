b = "Jaipur"
while True:
 a = input('Enter the password: ')
 if a == b :
   print ("Welcome to your system ")
   break
 else :
   print ("Please try again ")
 
b = "admin"
c = 0
while True:
 a = input('Enter the password: ')
 if a == b :
  print ("password accepted! ")
  break
 else :
  c += 1
  if c == 3 :
   print ('Account Locked')
   break
  else :
   print ("Try Again ")


a = 0
while True :
 b = input('enter the amount ')
 if b == 'stop' :
  print ("Total Bill:", a)
  break
 c = float(b)
 if c < 0 :
  print ("Total Bill:", a)  
  break
 a += c



a = int(input('enter a number '))
b = 2
while a%b != a
 b += 1
 if b == a :
  print ("prime number")
 else :
  print (b)
 
