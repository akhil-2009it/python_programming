

num=int(input("enter the number"))

count=0

if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
            
    if count==2:
        print("no is prime no")
    else:
        print("no is not prime no")