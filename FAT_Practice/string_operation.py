#11.  Write a program that takes a string as input and determines if it's a valid palindrome. 
# The program should ignore all non-alphanumeric characters and be case-insensitive. 
# For example, "A man, a plan, a canal: Panama" should return True.
import random
import string
def onlyAN(str):
    nstr = ''
    for c in str:
        if c in ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"):
            nstr += c
    return nstr.lower()

def reverse(str):
    str = onlyAN(str)
    nstr = ''
    for c in str:
        nstr = c+nstr
    return nstr

str = "A man, a plan, a canal: Panama" #''.join(random.choices(string.ascii_letters + string.digits, k=8))
if onlyAN(str) == reverse(str):
    print(True)
else:
    print(False)