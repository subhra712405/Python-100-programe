while(1):

    a=[]
    list=int(input("enter the size of list"))
    for i in range(list):
        val=int(input("enter the value"))
    
        a.append(val)
        a.sort()
    print("the largest number in the list ",a[-1])