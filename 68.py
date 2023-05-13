
n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
print("the array is ",r)
maximum=r[0]
for i in range(len(maximum)):
    if r[i] > maximum:
        maximum=r[i]

print("the largest number is ",maximum)