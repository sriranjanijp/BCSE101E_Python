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

#Find the sum of all even numbers in a list (using recursion)
def sum_rev(listin,length):
    if length == 0:
        return 0
    else:
        return listin[length-1]+sum_rev(listin,length-1)
    
print(sum_rev([1,1,1,1,1,1,1],7))

#Check if a number is prime (using recursion)
def prime(n,m=2):
    if n%m == 0:
        return False
    elif m*m>n:
        return True
    return prime(n,m+1)
    
print(prime(13))

#Remove all occurrences of an element from a list (using recursion)
def remove_element(lst, element):
    if not lst:
        return []
    if lst[0] == element:
        return remove_element(lst[1:], element)
    return [lst[0]] + remove_element(lst[1:], element)

lst = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
result = remove_element(lst, element_to_remove)
print(result)

#Calculate the sum of digits of a number (using recursion)
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

num = 12345
result = sum_of_digits(num)
print(result)

#Find the greatest common divisor of two numbers (using recursion)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = 48
num2 = 18
result = gcd(num1, num2)
print(result)

#Implement binary search on a sorted list (using recursion)
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)

