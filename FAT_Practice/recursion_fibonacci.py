#Fibonacci sequence: Implement a recursive function to generate the nth Fibonacci number.
def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))