d={}
n=int(input("enter  the nnumber of pair  key value :"))
for  i in range((n)):
    key=input("key name"+str(i+1)+":")
    value=int(input("key value"+str(i+1)+":"))
    d[key]=value
k=d.keys()
print("the key in dicctionay",k)