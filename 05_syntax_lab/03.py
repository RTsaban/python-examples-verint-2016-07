from random import randint 

num = randint(1, 10000)

sum=0
while (num>0):
    sum+=num%10
    num/=10

print sum