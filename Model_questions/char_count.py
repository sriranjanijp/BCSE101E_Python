#Count the occurrence of each character in a string (case-insensitive)
def count(str,char):
    count = 0
    str = str.lower()
    for i in str:
        if i == char:
            count += 1
    return count
print(count("HongJooNg",'n'))