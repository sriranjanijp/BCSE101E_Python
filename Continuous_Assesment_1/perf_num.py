'''
(Perfect number) A positive integer is called a perfect number if it is equal to the
sum of all of its positive divisors, excluding itself. For example, 6 is the first perfect
number, because The next is
DISPLAY ALL perfect numbers between 1 and 10,000. Write a program to find these
four numbers.'
'''
for j in range(10000):
    num = j
    sum = 0
    for i in range (1,num,1):
        if (num%i==0):
            sum = sum + i
    if (sum == num):
        print(num)