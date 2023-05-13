import math
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
num1=int(input("ener the number  :"))
num2=int(input("enter the number  :"))    
print(gcd(num1,num2))
