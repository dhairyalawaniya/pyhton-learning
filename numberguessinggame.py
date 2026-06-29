a = 57
print ('Hi! welcome to the number guessing game, you have six tries to guess the number')
b = 1
while b <=6:
    num = int(input('guess the number '))
    if num == a :
        print (f"Congrats! you guessed the number in {b} try")
        break
    elif num > a :
        print ('you guessed to high!')
    else :
        num < a 
        print ('you guessed the number too low')
    b += 1   
    print ('you lost')