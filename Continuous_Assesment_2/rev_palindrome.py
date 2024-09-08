# (Palindrome integer)
# Write the functions with the following headers:

# Return the reversal of an integer, e.g., reverse(456) returns 654
# def reverse(number):
#     pass

# Return true if number is a palindrome
# def isPalindrome(number):
#     pass

# Use the reverse function to implement isPalindrome.
# A number is a palindrome if its reversal is the same as itself.
# Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.

import random
def reverse(num):
    rev = 0
    while (num!=0):
        rev = (rev*10) + (num%10)
        num = num//10
    return rev
    
def isPalindrome(num):
    if num == reverse(num):
        return True 
    else:
        return False

userinput = random.randint(1,100000)
print("Your input:",userinput)
print("Is it a palindrome:",isPalindrome(userinput))