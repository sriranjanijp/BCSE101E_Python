#Generate all possible substrings of a string
def generate_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

s = "abc"
result = generate_substrings(s)
print(result)
