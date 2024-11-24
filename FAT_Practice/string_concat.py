# Implement a function that performs basic string compression using the counts of repeated characters. 
# For example, the string "aabcccccaaa" would become "a2b1c5a3".
# If the compressed string would not become smaller than the original string, your function should return the original string.
strin = "aabcccccaaa"
def concat(strin):
    strin = strin+' '
    t = strin[0]
    fin = ''
    count = 0
    for c in strin:
        if t==c:
            count += 1
        else:
            fin += t+str(count)
            count = 1
        t = c
    return fin

print(concat("aabcccccaaa"))