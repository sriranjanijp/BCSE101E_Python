'''
(Financial application: compute future tuition) Suppose that the tuition for a university
is Rs100000 this year and increases 8.5% every year. Write a program that
computes the tuition in ten years and the total cost of four years' worth of tuition
starting ten years from now.

NOTE: Take random data wherever required. ignore given test case. Generate 4 test cases.
'''
import random
for j in range (4):
    tuition = random.randint(100000,1000000)
    rate = 8.5/100
    amount = 0
    cost = 0
    print("Initial tuition: ",tuition)
    for i in range (1,11,1):
        interest = tuition*rate
        amount = tuition+interest
        tuition = amount
        print("Tuition after",i," years: ", round(tuition,4))
    cost = tuition
    for j in range (11,14,1):
        interest = tuition*rate
        amount = tuition+interest
        tuition = amount
        cost = cost + tuition
        print("Tuition after",j," years: ", round(tuition,4))
    print("Cost of a degree after 10 years: ",round(cost,4))