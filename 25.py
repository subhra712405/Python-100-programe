a=[]
list1=int(input("enter the sizeo of list  :"))
for i in range(list1):
    val=int(input("enter the eliment of list   :"))
    a.append(val)
print("1st original list is  ",a)

b=[]
list2=int(input("enter the size of list   :"))
for i in range(list2):
    val=int(input("enter the eliment of list   :"))
    b.append(val)
print("the second original list is  ",b)

print("the common eliment in list is ",set(a).intersection(set(b)))
