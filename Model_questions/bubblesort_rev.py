swap = True
listin = [1,2,3,4,5,6,7,8,9]
i = 0
while swap == True:
    swap = False
    for i in range(0,len(listin)-1):
        if listin[i]<listin[i+1]:
            listin[i],listin[i+1] = listin[i+1],listin[i]
            swap = True

print(listin)