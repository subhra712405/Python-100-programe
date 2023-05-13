a=[]
list1=int(input("enter the size of list :"))
for i in range(list1):
    val=int(input("enter the eliment :"))
    a.append(val)
b=[]
list2=int(input("enter the size of list"))
for i in range(list2):
    val=int(input("enter the eliment :"))
    b.append(val)

print("the union of two list is ",set(a).union(set(b)))