def isPalindrome(s):
    s=s.lower()
    return s == s[::-1]

str_temp = []
str = input("enter the text  :")
             
words =str.split() 
# print(words, len(words))
for i in range(len(words)):
    if(isPalindrome(words[i])):
        str_temp.append(words[i])
print(str_temp)       
str_temp.sort()
# print(str_temp)
for word2 in str_temp:
    if len(str_temp)==1:
        str_temp.remove(word2)
print("the longest palindrom is   :",str_temp[0])