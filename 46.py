count=0
with open("C:\\Users\\subhr\\OneDrive\\Desktop\\python\\29.py","r") as fl:
    line=fl.read()
    split=line.split()
    count+=len(split)
print("the  number of word is  :",count)