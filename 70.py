
n=int(input("enter the rows :"))
m=int(input("enter the colums :"))
r=[]
for  i in range(n):
    c=[]
    for j in range(m):
        v=int(input())
        c.append(v)
    r.append(c)
even_sum=0
for row in r:
    for val in row:
        
        if val%2==0:
            even_sum=even_sum+(val)
print("the sum of even number is ",even_sum)
