'''
(Financial application: loan amortization schedule) The monthly payment for a
given loan pays the principal and the interest. The monthly interest is computed by
multiplying the monthly interest rate and the balance (the remaining principal).
The principal paid for the month is therefore the monthly payment minus the
monthly interest. Write a program that lets the user enter the loan amount, number
of years, and interest rate, and then displays the amortization schedule for the loan.
Here is a sample run:
'''
loan = 10000
annual_rate = 7
years = 1
months = years*12
monthly_rate = annual_rate/1200
monthly_payment = loan* monthly_rate / (1 - (1 + monthly_rate) ** -months)
print("Balance -",loan)
print("Annual rate -",annual_rate)
print("Number of years -",years)
print("Total payment -",((loan*annual_rate*years)/100)+loan)
print("Monthly payment -",monthly_payment)

total_payment = 0
balance = loan

print(f"{'Payment#':<10}{'Interest':<15}{'Principal':<15}{'Balance':<15}")
    
for i in range(1, years * 12 + 1):
    interest = balance * monthly_rate
    principal = monthly_payment - interest
    balance = balance - principal
    total_payment += monthly_payment
    
    if balance < 0:
        balance = 0

    print(f"{i:<10}{interest:<15.2f}{principal:<15.2f}{balance:<15.2f}")