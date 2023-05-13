string =input("enter text  :")
index = -1
print(type(index))
fnc = ""
for i in string:
    if string.count(i) == 1:
        
        fnc += i
        break
    else:
        index += 1


