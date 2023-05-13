d={}
n=int(input("enter  the nnumber of pair  key value :"))
for  i in range((n)):
    key=input("key name"+str(i+1)+":")
    value=int(input("key value"+str(i+1)+":"))
    d[key]=value
total=0
for value in d.values():
    if value%2==0:
        total=total+value
print("the sum of all even number ",total)