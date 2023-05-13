def chake(str):
    alphabate="abcdefghijklmnopqrstuvwxyz"
    for char in alphabate:
        if char not in str.lower():
            return False
    return True
str=input("enter txt  :")
if(chake(str)==True):
    print("it is a pangram")
else:
    print("it is not pangram")
