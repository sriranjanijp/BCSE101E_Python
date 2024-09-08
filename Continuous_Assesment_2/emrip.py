# Display first 100 emrips as 10 per line
# Emrips are prime numbers whose palindrome is also a prime number

def reverse(num):
    rev = 0
    while (num!=0):
        rev = (rev*10) + (num%10)
        num = num//10
    return rev
    
def emrip(num):
    rev = reverse(num)
    if rev != num:
        rdivisors = 0
        ndivisors = 0
        for i in range(2,rev,1):
            if rev%i == 0:
                rdivisors+=1
        for i in range(2,num,1):
            if num%i == 0:
                ndivisors+=1
        if rdivisors == 0 and ndivisors == 0:
            return num
        else:
            return False
    else:
        return False

t=12
j = 1
i = 0
while (j<=100):
    if emrip(t) != False:
       print(f"{emrip(t):4}",end=" ")
       i+=1
       j+=1
    if i == 10:
        print()
        i = 0 
    t+=1