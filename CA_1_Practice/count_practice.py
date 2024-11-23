#Write a Python program that reads an unspecified number of integers, determines
#how many positive and negative values have been read, and computes the total
#and average of the input values (not counting zeros). Your program ends with the
#input either 0 or no. of elements read is 20. Display the average as a floating-point number.

#Note: Take random data between -500 to 500. ignore given test case. Generate 4 test cases.
import random
for i in range(4):
    i = 0
    neg = 0
    pos = 0
    total = 0
    while i < 20:
        num = random.randint(-500,500)
        i += 1
        if num < 0:
            neg += 1
            total += num
        elif num>0:
            pos += 1
            total += num
        else:
            break
    print(f"{neg} negative numbers have been entered")
    print(f"{pos} positive numbers have been entered")
    print("Total is ",total)
    print("Average is ",total/i)