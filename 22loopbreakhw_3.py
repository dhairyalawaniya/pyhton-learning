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
