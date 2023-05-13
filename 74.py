

n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
    
# print(r)


p=int(input("enter the rows :"))
q=int(input("enter the colums :"))
s=[]
for i in range(p):
    d=[]
    for i in range(q):
        val=int(input("enter the eliment"))
        d.append(val)
    s.append(d)
# print(s)

if m and n != p and q :
    print("the matrix row and colum is not same ")
