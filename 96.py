a=[]
list=int(input("enter the size of list"))
for i in range(list):
    val=int(input("enter the value"))
   
    a.append(val)
    a.sort()
print("the original list is ",a)
b=[]
list1=int(input("enter the size of list"))
for j in range(list1):
    val1=int(input("enter the value"))
   
    b.append(val1)
    b.sort()
print("the original list is ",b)
r=set(a).intersection(set(b))
print("the intersection of two list is ",r)