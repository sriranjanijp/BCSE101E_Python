import random
d = {"apple": 10,
    "banana": 20,
    "cherry": 15,
    "date": 30,
    "fig": 25}
my = 'fig'
a = d.get(my,"Key not found")
print(list(d.keys()))
s1 = set(random.sample(range(1,21),10))
s2 = set(random.sample(range(1,21),5))
s3 = set(random.sample(range(1,21),3))
print(s1)
print(s2)
