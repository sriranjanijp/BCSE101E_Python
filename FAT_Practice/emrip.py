# (Emirp) An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime. 
# For example, both 17 and 71 are prime numbers, so 17 and 71 are emirps. Write a program that displays the first 100 emirps. 
# Display 10 numbers per line and align the numbers properly

def reverse(num):
    rev = 0
    while num != 0:
        rev = rev*10 + num%10
        num //=10
    return rev

def is_emrip(num):
    rev = reverse(num)
    if rev != num:
        rdivisor = 0
        ndivisor = 0
        for i in range(2,num,1):
            if num%i==0:
                ndivisor += 1
        for i in range(2,rev,1):
            if rev%i==0:
                rdivisor += 1
        if rdivisor == 0 and ndivisor == 0:
            return True
        else:
            return False
    else:
        return False
    
i = 0
n = 10
while i<100:
    if is_emrip(n) == True:
        print(f"{n:^7}",end='')
        i += 1
        if i%10 == 0:
            print()
    n += 1