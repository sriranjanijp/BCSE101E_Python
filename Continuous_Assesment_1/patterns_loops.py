'''
Display the below
NOTE: Take input as no.of lines between 1 to 10. Display one by one in the order as same program.
1
12
123
1234
12345
123456

123456
12345
1234
123
12
1
     1
    21
   321
  4321
 54321
654321
'''
import random
for j in range(4):
    lines = random.randint(2,10)

    for i in range(1,lines+1,1):
        for j in range(1,i+1,1):
            print(j,end='')
        print()
    print()

    for i in range(lines+1,1,-1):
        for j in range(1,i,1):
            print(j,end='')
        print()
    print()

    for i in range(1,lines+1,1):
        for j in range(lines-i,0,-1):
            print(" ",end='')
        for j in range(i,0,-1):
            print(j,end='')
        print() 
    print()    