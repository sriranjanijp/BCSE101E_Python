#Display a pyramid

import random
lines = random.randint(7,10)

for i in range(1,lines+1,1):
    for j in range(lines,i,-1):
        print(" ",end=' ')
    for j in range(0,i-1,1):
        print(2**j,end=' ')
    for j in range(i-1,-1,-1):
        print(2**j,end=' ')
    print()
print()
lines = random.randint(3,15)

for i in range(1,lines+1,1):
    for j in range(lines,i,-1):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    for j in range(2,i+1,1):
        print(j,end=' ')
    print()