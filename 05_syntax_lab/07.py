from random import randint 

num = randint(1,100) 

while True:
    input = int (raw_input())
    if input > num:
        print "too big"
    elif input < num:
        print "too small"
    else:
        print "got it"
        break

