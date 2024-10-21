str = "Captain HongJoong"
str = str.lower()
str = str.replace(' ','')
newstr = ''
for i in range (len(str)-1,-1,-1):
    newstr = newstr + str[i]
print(str)
print(newstr)
if str == newstr:
    print("String is a palindrome")
else:
    print("String is not a palindrome")