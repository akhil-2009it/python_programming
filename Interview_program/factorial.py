


num = (int(input("enter the no of your choice  = ")))
fact=1
if num< 0:
    print("wrong entry")

if num ==1:
    print("fact is 1")

if num >1:
    for i in range(2, num+1):
        fact = fact*i
    print(fact)