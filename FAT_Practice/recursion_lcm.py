#6.  LCM Calculation: Question: Write a recursive function to find the Least Common Multiple (LCM) of two positive integers without using the GCD method.
def lcm(a,b,multiple = None):
    if multiple == None:
        multiple = max(a,b)
    if multiple%a == 0 and multiple%b == 0:
        return multiple
    return lcm(a,b,multiple+max(a,b))

print(lcm(24,34))