from random import randint 

sum = 0 
for i in range(1,7) :
    num = randint(1, 10)
    sum += num
    
if (sum % 7) == 0 :
    print "Boom"
    