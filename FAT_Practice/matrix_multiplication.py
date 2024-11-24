# Write a Python program that reads two matrices of size n x m and m x p from the user and performs matrix multiplication. 
# The program should check if matrix multiplication is possible before proceeding.
import random
n = 3
m = 3
p = 4
a = [[random.randint(-50,50) for _ in range(m)]for _ in range (n)]
b = [[random.randint(-50,50) for _ in range(p)]for _ in range (m)]
c = [[random.randint(-50,50) for _ in range(p)]for _ in range (n)]
if len(a[0]) != len(b):
    print("Matrix multiplication not possible")
else:
    print("Matrix multiplication possible")
    for i in range (n):
        for j in range (p):
            c[i][j] = 0
            for k in range(m):
                c[i][j] += a[i][k]*b[k][j]
    for p in c:
        for d in p:
            print(f"{d:^6}",end='')
        print( )