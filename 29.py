n=input("enter binary number  :")
l=list(n)
l.reverse
sum=0
for i in range(len(l)):
    sum=sum+int(l[i])*2**i
print("the decimle numer of",n,"is",sum)
    
