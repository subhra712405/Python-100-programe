str1=input("enter str :")
str2=input("enter 2ndstr :")


if len(str1)!=len(str2):
    print("strings are not anagram   :")
else:
    if sorted(str1)==sorted(str1):
        print("strings are anagram   :")
    else:
        print("strings are not anagram  :") 