reverse=""
while True:
    input = raw_input();
    if len(input)==0 : break
    reverse = input + "\n" + reverse

print reverse