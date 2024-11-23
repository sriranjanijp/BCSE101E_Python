#Arithmetic Sequence Sum: Question: Write a recursive function to find the sum of n terms of an arithmetic sequence with first term a and common difference d.
def AP(n,a,d):
    if n==1:
        return a
    else:
        return a+(n-1)*d + AP(n-1,a,d)
    
print(AP(10,5,2))