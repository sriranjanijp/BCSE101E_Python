#Remove duplicates from a list while preserving order
listin = [1,2,3,4,5,2,4,2,4,6,7,8,7,3]
i = j = 0
while i<len(listin):
    j = i+1
    while j<len(listin):
        if listin[i]==listin[j]:
            listin.pop(j)
        j += 1
    i += 1
print(listin)