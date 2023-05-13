a=[]
si=int(input("enter the sizze of list"))
for i in range(si):
    val=int(input("enter the eliment :"))
    a.append(val)
b=[]
di=int(input("enter the size of list"))
for i in range(di):
    val=(int(input("enter the elimnet")))
    b.append(val)
de=set(a).symmetric_difference(set(b))
print("the difference is ",de)
