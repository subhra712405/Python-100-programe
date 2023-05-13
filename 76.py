n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
print(r)
trace=0
for i in range(len(r)):
    trace=trace+r[i][i]
print("the trace is ",trace)