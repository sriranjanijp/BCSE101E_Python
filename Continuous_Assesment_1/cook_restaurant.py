t = int(input())
index = []

for i in range(t):
    count = 0
    n = int(input())
    ingr = list(map(int, input().strip().split()))[:n]
    m = int(input())
    for j in range(0,len(ingr),1):
        if ingr[j] == m:
            index.append(j)
            count = 1
    if count == 0:
        index.append(-1)

    
for i in range(0,len(index),1):
    print(index[i])