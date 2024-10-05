#Write a program to find the number of times each element occurs in the list.
lisin = [1,2,3,2,3,4,3,5,6,5,3,4,6,1]
test = 0
element = 0
count = 0
i = 0
while i<len(lisin):
    test = lisin[i]
    l = len(lisin)
    j = 0
    while j<l:
        element = lisin[j]
        if element == test:
            count += 1
            lisin.pop(j)
        l = len(lisin)
        j += 1
    print(f"{test} occurs {count} times")
    count = 0
    i += 1

