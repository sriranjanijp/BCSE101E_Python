#Find all prime factors of a number
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

num = 16
result = prime_factors(num)
print(result)

n = 16
factors = []
i = 2
while i*i<=n:
    if n%i == 0:
        factors.append(i)
        n = n//i
    else:
        i += 1
if n>1:
    factors.append(n)
print(factors)