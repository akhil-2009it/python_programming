

def fact(n):
    
    return 1 if(n == 0 or n == 1) else n*fact(n-1)


n =6

print("factrial is", fact(n))