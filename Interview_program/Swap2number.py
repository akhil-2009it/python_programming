

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))


#num1 = 13
#num2 = 14

#Approch1
# temp=num1
# num1=num2
# num2=temp

#approch2
# num1,num2=num2,num1

#Approch3

num2=num1+num2
num1=num2-num1
num2=num2-num1


print("Now num1 =",num1)
print("Now num2 =",num2)

