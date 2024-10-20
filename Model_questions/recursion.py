#Calculate the factorial of a number (using recursion)
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#Reverse a string (using recursion)
def str_rev(str,length = 0):
    if length == 0:
        return ''
    else:
        return(str[length-1])+str_rev(str,length-1)

str = 'aeiou'   
length = len(str)
print(str_rev(str,length))

