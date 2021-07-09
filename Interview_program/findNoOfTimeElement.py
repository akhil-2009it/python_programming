


mylist = [11,44,11,22,66,33,11,88,11,55]

x = 11

count=0

for i in mylist :
    if i==x:
        count=count+1

print("{} is of {} time present".format(x,count))