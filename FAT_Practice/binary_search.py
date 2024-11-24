listin = [1,2,3,4,5,6,7,8,9,10]
e = 8
c = 0
low = 0
high = len(listin)-1
while low<=high:
    mid = low+(high-low)//2
    if listin[mid]<e:
        low = mid+1
    elif listin[mid]>e:
        high = mid-1
    else:
        print(f"Element found at index - {mid}")
        c = 1
        break
if c==0:
    print("Element not found")