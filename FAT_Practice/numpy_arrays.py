import numpy as np
# A 1-D array called zeros having 10 elements and all the elements are set to zero.
print(np.zeros(10))
# A 1-D array called vowels having the elements ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’.
vowels = np.array(['a','e','i','o','u'])
print(vowels)
# 3. A 2-D array called ones with 2 rows and 5 columns, all set to 1 and dtype as int.
print(np.ones((2,5),dtype = int))
# A 2-D array called myarray2 using arange() with 3 rows and 5 columns, start=4, step=4, dtype=float.
print(np.arange(4,61,4,dtype=float).reshape(3,5))
array = np.arange(4,61,4,dtype=float).reshape(3,5)
print(f"HEy - Dimensions: {array.ndim}, Shape: {array.shape}, Size: {array.size}, Data type: {array.dtype}, Itemsize: {array.itemsize}")
print(array[::-1,::-1])
print(array.T)
print(np.sort(array,axis=0))

myarray4 = np.arange(-1, 9.5, 0.25).reshape(14, 3)
myarray4_split = np.array_split(myarray4, 3)
print("myarray4 split into 3 parts:")
for i, part in enumerate(myarray4_split, 1):
    print(f"Part {i}:\n", part)

print(np.sum(array,axis=0))