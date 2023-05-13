

n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
    
if n==m:
    print("it is a symmetric matrix :")
else:
    print("not a symmetric matrix ;")
          