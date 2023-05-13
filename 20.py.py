a=[]
list=int(input("enter the size of list"))
for i in range(list):
        val=int(input("enter the value"))
    
        a.append(val)
print("the original list is ",a)
a.reverse()
print("thr reversed list is ",a)