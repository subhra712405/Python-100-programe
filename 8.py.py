while(1):
    a=[]

    size=int(input("enter the size you want"))
    for i in range(size):
        val=int(input("enter the eliment"))
        for i in range(val):
            a.append(val)
            
    print(list(set(a)))