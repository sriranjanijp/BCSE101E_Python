'''
(Math: pentagonal numbers) A pentagonal number is defined as: n(3n-1)/2
n=1,2,…. So, the first few numbers are 1, 5, 12, 22, .... 
Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal numbers with 10 numbers on each line.
'''
def getPentagonalNumber(n):
    for i in range(n,n+10,1):
        pentnum=(i*(3*i-1))/2
        print(f"{int(pentnum):5}",end=" ")
    print()
    
for j in range(1,101,10):
    getPentagonalNumber(j)