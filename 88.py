d={}
n=int(input("enter  the nnumber of pair  key value :"))
for  i in range((n)):
    key=input("key name"+str(i+1)+":")
    value=int(input("key value"+str(i+1)+":"))
    d[key]=value
sorted_dict = sorted(d.items(), key=lambda x: x[1])
str=dict(sorted_dict)
print("the sorted bby vlaue is ",str)