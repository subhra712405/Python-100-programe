

n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
A=r

p=int(input("enter the rows :"))
q=int(input("enter the colums :"))
s=[]
for i in range(p):
    d=[]
    for i in range(q):
        val=int(int(input("enter the eliment")))
        d.append(val)
    s.append(d)
S=s
total=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        total[i][j]=A[i][j]+S[i][j]
    

print("the addition is",total)