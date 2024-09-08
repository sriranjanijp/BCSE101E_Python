#Write a Python program that reads an unspecified number of integers, determines
#how many positive and negative values have been read, and computes the total
#and average of the input values (not counting zeros). Your program ends with the
#input either 0 or no. of elements read is 20. Display the average as a floating-point number.

#Note: Take random data between -500 to 500. ignore given test case. Generate 4 test cases.

import random
neg = 0
pos = 0
i = j = 1
total = 0
while j<=4:  #Generate 4 test cases
    i = 1
    while i<=20:
        num = random.randint(-500,500)
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
        else:
            pass
        print(num, end=" ")
        total = total + num
        i = i+1
    avg = total/i
    print("\nAverage is:",avg)
    print("Number of positive values:",pos)
    print("Number of negative values:",neg)
    j = j+1