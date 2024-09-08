'''
(Occurrence of max numbers) Write a program that reads integers between -1000 to 1000, finds the
largest of them, and counts its occurrences. Assume that the input ends with either number
0 or read 25 numbers. Suppose that you entered 3 5 2 5 5 5 0; the program finds that the
largest number is 5 and the occurrence count for 5 is 4.
'''

import random
count = 0
num = random.randint(-1000,1000)
print(num)
large = num
i = 1
while (num!=0 and i<25):
    if num>large:
        large = num
        count = 1
    elif num<large:
        pass
    else:
        count +=1
    i += 1
    num = random.randint(-1000,1000)
    print(num)
print("The largest number is: ",large)
print("Occurances: ", count)