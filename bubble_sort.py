#Write a program to sort (using Bubble sort algorithm) the given list of elements 
# without using built-in function.

lisin = [10,9,8,7,6,5,4,3,2,1]
i = 0
swap = True
while swap == True:
    i = 0
    swap = False
    while i<len(lisin)-1:
        if lisin[i]>lisin[i+1]:
            lisin[i], lisin [i+1] = lisin [i+1], lisin[i]
            swap = True
        i += 1
print(lisin)

element = 17
low = 0
high = len(lisin)-1
c = 0
while low<=high:
    mid = low + (high-low)//2
    if lisin[mid]==element:
        print("Element found")
        c = 1
        break
    elif lisin[mid]<element:
        low = mid + 1
    else:
        high = mid - 1
if c==0:
    print("Element no found")  
