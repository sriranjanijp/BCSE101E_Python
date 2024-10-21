#Generate Fibonacci sequence up to n terms (using recursion)
def Fibonacci(n): 
    if n<= 1: 
        return n
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

for i in range (10):
    print(Fibonacci(i),end=' ')

