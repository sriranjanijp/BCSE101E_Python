#3. Set Operations:
#Design a menu-driven program using user-defined functions to perform various set operations such as:
#- Add an element to the set
#- Remove an element from the set
#- Find the union of two sets
#- Find the intersection of two sets
#- Find the difference between two sets
#- Find the symmetric difference of two sets
#- Check if a set is a subset of another set
#- Display the set
import random
#- Add an element to the set
def setAdd(s,e):
    s.add(e)
    return s
#- Remove an element from the set
def setRemove(s,e):
    s.remove(e)
    return s
#- Find the union of two sets
def setUnion(s1,s2):
    return s1 | s2         #s1.union(s2)
#- Find the intersection of two sets
def setIntersection(s1,s2):
    return s1&s2
#- Find the difference between two sets
def setDifference(s1,s2):
    return s1-s2
#- Find the symmetric difference of two sets
def setSymmetricDiff(s1,s2):
    return s1^s2
#- Check if a set is a subset of another set
def setSubset(s1,s2):
    if s1 <= s2:
        return True
    else:
        return False
def setDisplay(s):
    print(s)
s1 = set(random.sample(range(1,21),10))
s2 = set(random.sample(range(1,21),5))
s3 = set(random.sample(range(1,21),3))
e = random.randint(1,20)
while True:
    print("1: Add an element to the set")
    print("2: Remove an element from the set")
    print("3: Find the union of two sets")
    print("4: Find the intersection of two sets")
    print("5: Find the difference between two sets")
    print("6: Find the symmetric difference of two sets")
    print("7: Check if a set is a subset of another set")
    print("8: Display the set")
    c = random.randint(1,15)
    print("Enter your choice: ",c)
    if c==1:
        print("Enter the set: ",s1)
        print("Enter the element to add: ",e)
        print(setAdd(s1,e))
        break
    elif c==2:
        print("Enter the set: ",s1)
        print("Enter the element to remove: ",e)
        print(setRemove(s1,e))
        break
    elif c==3:
        print("Enter the set 1: ",s1)
        print("Enter the set 2: ",s2)
        print(setUnion(s1,s2))
        break
    elif c==4:
        print("Enter the set 1: ",s1)
        print("Enter the set 2: ",s2)
        print(setIntersection(s1,s2))
        break
    elif c==5:
        print("Enter the set 1: ",s1)
        print("Enter the set 2: ",s2)
        print(setDifference(s1,s2))
        break
    elif c==6:
        print("Enter the set 1: ",s1)
        print("Enter the set 2: ",s2)
        print(setSymmetricDiff(s1,s2))
        break
    elif c==7:
        print("Enter the set 1: ",s1)
        print("Enter the set 2: ",s3)
        print(setSubset(s3,s1))
        break
    elif c==8:
        print("Enter the set: ",s1)
        setDisplay(s1)
        break
    else:
        print("Enter the correct value: ")
        c = random.randint(1,8)