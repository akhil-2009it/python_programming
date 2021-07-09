
mylist = ["akhil","ritika","atharv","atharv"]

name = "atharv"

n=2
count =0

for i in range(0,len(mylist)):
    if mylist[i]==name:
        count=count+1
        if count==n:
            del mylist[i]

print(mylist)

