# to check num is having 2 factor 1 and itself



num = 8
count = 0

if num>0:
    for i in range(1,num+1):
        if (num%i) == 0:
            count = count +1


    if count==2:
        print("Number is prime")
    else:
        print("Number is not prime")
