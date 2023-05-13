# Diffrnce between two list  :
a=[]
list1=int(input("enter the sizeo of list  :"))
for i in range(list1):
    val=int(input("enter the eliment of list   :"))
    a.append(val)
    aa=sum(a)
# print("1st original list is  ",a)

b=[]
list2=int(input("enter the sizeo of list  :"))
for i in range(list2):
    val=int(input("enter the eliment of list   :"))
    b.append(val)
    bb=sum(b)
# print("1st original list is  ",b)
print("the uncommon eliment in two list is",set(a).intersection(set(b)))
if list1==list2:
    print("none difference")
else:
    print("the seze of list different list1 size is",list1,"the list2 size is",list2)

    if aa==bb:
        print("none difference")
    else:
        print("the sum of list is diferrent the sum of list1 is ",aa,"the sum of list2 is",bb)


         





