
import numpy
n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
tr=numpy.transpose(r)
print("original matrix is",tr)
print("transpose matrix is",tr)