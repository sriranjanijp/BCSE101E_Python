# Write a Python program that reads two matrices of size n x n and n x n from the user and performs matrix addition. 
# The program should check if matrix addition is possible before proceeding.
import random
import numpy as np
n = 3
m = 3
a = [[random.randint(-50,50) for j in range(n)]for i in range(n)]
b = [[random.randint(-50,50) for j in range(n)]for i in range(n)]
c = [[0 for j in range(n)]for i in range(n)]
print("      Matrix 1             Matrix 2")
for w,p in zip(a,b):
    for d in w:
        print(f"{d:^6}",end='')
    print("    ",end='')
    for q in p:
        print(f"{q:^6}",end='')
    print()
print()
print("   Added matrix")
for i in range(n):
    for j in range(n):
        c[i][j] = a[i][j] + b[i][j]

for a in c:
    for d in a:
        print(f"{d:^6}",end='')
    print()