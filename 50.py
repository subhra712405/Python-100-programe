import re
n=input("enter password :")
char=0
while(1):
    if (len(n)<=8) :
        char=-1
        break
    elif not re.search("[a-z]",n):
        char=-1
        break
    elif  not re.search("[A-Z]",n):
        char=-1
        break
    elif not re.search("[0-9]",n):
        char=-1
        break
    elif not re.search("[_@$]",n):
        char=-1
        break
    elif not re.search("[/s]",n):
        char=-1
        break
    else:
        char=0
        print("valid password :")
if char==-1:
    print("invalid password :")
    