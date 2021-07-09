#5 = 1*2*3*4*5 = 120

num=5

factorial = 1

if num<0:
    print("No fac")
elif num==0:
    print("fact is 1")
else:
    for i in range (1, num+1):
        factorial= factorial*i 
    print("fact is", factorial)