def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input("enter the number"))
if n<0:
    print("factorial does not exisit")
else:
    print("the factorial is",fact(n))