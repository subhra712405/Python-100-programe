import numpy as np
n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
egienvalues=np.array(r)
rgi=np.linalg.matrix_rank(egienvalues)
print("the rank of matrix is ",rgi)