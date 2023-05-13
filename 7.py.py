while(1):

    a=[]

    mylist=int(input("enter the size"))
    for i in range(mylist):
        val=int(input("enter the ele"))
        for i in range(val):
            a.append(val)
        a.sort()
        
    print("the minimum value is ",min(a))
    print("the maximum number is",max(a))