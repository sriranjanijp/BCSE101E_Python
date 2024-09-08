# (Sum the digits in an integer)
# Write a function that computes the sum of the digits in an integer.
# Use the following function header:
#
# def sumDigits(n):
#
# For example, sumDigits(234) returns 9 (2 + 3 + 4).
# (Hint: Use the % operator to extract digits, and the // operator to remove the extracted digit.
# For instance, to extract 4 from 234, use 234 % 10 (which gives 4).
# To remove 4 from 234, use 234 // 10 (which gives 23).
# Use a loop to repeatedly extract and remove the digits until all the digits are extracted.)
#
# Write a test program that prompts the user to enter an integer and displays the sum of all its digits.

import random
def sumDigits(num):
    sum = 0
    while (num!=0):
        sum = sum + num%10
        num = num//10
    return sum

userinput = random.randint(1,10000)
print("The given number:",userinput)
print("The sum of digits is:",sumDigits(userinput))