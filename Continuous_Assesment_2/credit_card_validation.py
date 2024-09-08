'''
Write a program that prompts the user to enter a credit card number as a long integer and Display whether that card is valid or invalid.
Credit card numbers follow certain patterns. 
A credit card number must have between 13 and 16 digits. It must start with:

4 for Visa cards
5 for Master cards
37 for American Express cards
6 for Discover cards

The problem can be solved by using Luhn algorithm. 
Luhn check or the Mod 10 check, which can be described as follows (for illustration, consider the card number 4388576018402626):

Step 1. Double every second digit from right to left. If doubling of a digit results in a 
two-digit number, add up the two digits to get a single-digit number (like for 12:1+2, 18=1+8).

Step 2. Now add all single-digit numbers from Step 1. 
4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

Step 3. Add all digits in the odd places from right to left in the card number. 
6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

Step 4. Sum the results from Step 2 and Step 3. 37 + 38 = 75

Step 5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. 

#Return true if the card number is valid
def isValid(number):

#Get the result from Step 2
def sumOfDoubleEvenPlace (number):

# Return this number if it is a single digit, otherwise, return the sum of the two digits 
def getDigit(number):

#Return sum of odd place digits in number
def sumOfOddPlace (number):

#Return true if the digit d is a prefix for number
def prefixMatched (number, d):

#Return the number of digits in d
def getSize(d):

#Return the first k number of digits from number. If the #number of digits in number is less than k, return number.
def getPrefix (number, k):
'''
cardno = 4111111111111111
def getSize(cardno):
    size = 0
    while cardno != 0:
        cardno = cardno//10
        size+=1
    return size

def getDigit(num):
    if num>10:
        sum = 0
        while (num!=0):
            sum = sum + num%10
            num = num//10
        return sum
    else:
        return num

def sumOfDoubleEvenPlace(cardno):
    sum = 0
    while (cardno!=0):
        cardno = cardno//10
        x = 2*(cardno%10)
        digit = getDigit(x)
        sum = sum + digit
        cardno = cardno//10
    return sum

def sumOfOddPlace(cardno):
    sum = 0
    while (cardno!=0):
        x = cardno%10
        digit = getDigit(x)
        sum = sum + digit
        cardno = cardno//10
        cardno = cardno//10
    return sum

def getPrefix(cardno,num):
    t = (getSize(cardno)-num)
    x = cardno//(10**t)
    return x

def prefixMatched(cardno):
    y = getPrefix(cardno,1)
    if y==3 or y==4 or y==5 or y==6:
        return True
    else:
        return False

def isValid(cardno):
    if prefixMatched(cardno) == True:
        x = sumOfDoubleEvenPlace(cardno) + sumOfOddPlace(cardno)
        if x%10 == 0:
            ans = "Valid"
        else:
            ans = " Not Valid"
    else:
        ans = "Not Valid"
    return ans

print(isValid(cardno))