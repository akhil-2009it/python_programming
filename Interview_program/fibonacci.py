#0  1  1  2  3  5  8  13  21 ... no
#n1 n2
fib = (int(input("enter the number  = ")))
n1= 0
n2= 1

print(n1)
print(n2)

for i in range(2, fib):
    sum = n1+n2
    print(sum)
    n1=n2
    n2=sum
