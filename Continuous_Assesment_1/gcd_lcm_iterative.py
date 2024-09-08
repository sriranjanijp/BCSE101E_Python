'''
Write a program to compute the  greatest common divisor (GCD) and LCM (Least Common Multiple)  
of two integers (take random data between 50 and 500).
'''
import random
int1 = random.randint(50,500)
int2 = random.randint(50,500)
#GCD
gcd = 1
i = 1
while (i<=int1 and i<=int2):
    if (int1%i == 0 and int2%i == 0):
        gcd = i
    i += 1
print("The two numbers are: ",int1," and",int2)
print("GCD: ",gcd)

#LCM
prod = int1*int2
lcm = 1
while prod>=1:
    if (prod%int1==0 and prod%int2==0):
        lcm = prod
    prod -=1
print("LCM: ",lcm)
