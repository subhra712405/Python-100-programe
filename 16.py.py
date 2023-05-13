a=[]
list=int(input("enter the size of list"))
for i in range(list):
    val=int(input("enter the value"))
   
    a.append(val)
    
print("the original list is ",a)

num=int(input("chose a number from list which yuo chake"))
print(num,"occurence in the list",a.count(num))