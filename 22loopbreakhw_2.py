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
