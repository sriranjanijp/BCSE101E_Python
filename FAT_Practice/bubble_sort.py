listin = [10,9,8,4,7,6,5,4,3,2,1]
swap = True
while swap == True:
    i = 0
    swap = False
    while i<len(listin)-1:
        if listin[i]>listin[i+1]:
            listin[i],listin[i+1]=listin[i+1],listin[i]
            swap = True
        i += 1
print(listin)