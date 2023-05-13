  
while(1):
    sen=input("enter your string        :")
    count=0
    l=['a','e','i','o','u','A','E','I','O','U']
    for char in sen:
        if char in l:
            count=count+1
    print("number of vowel in sntence      :",count)