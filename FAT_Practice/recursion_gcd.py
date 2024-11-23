#Greatest Common Divisor (GCD): Write a recursive function to find the GCD of two numbers using the Euclidean algorithm.
def gcd(n1,n2):
    if n2>n1:
        n1,n2 = n2,n1
    if n2==0:
        return n1
    return gcd(n1%n2,n2)
print(gcd(36,27))