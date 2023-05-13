while(1):
    a=[]
    mylist=int(input("enter the size of list"))
    for  i in range(mylist):
            val=int(input("enter the eliment"))
            
            a.append(val)
            a.sort()
    print("the second largest number is",(a[-2]))     
