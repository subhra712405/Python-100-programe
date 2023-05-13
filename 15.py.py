while(1):
    a=[]
    list=int(input("enter the size of your list"))
    for i in range(list):
        val=int(input("enter the eleiment"))
        
        a.append(val)

        
        total=sum(a)
        final=total/list
    print("the average value in the list is  :",final)
