# 5. Write a program to read a list of elements. Modify this list so that it 
# does not contain any duplicate elements, i.e., all elements occurring 
# multiple times in the list should appear only once.
lisin = [3,5,7,2,5,8,4,2,5,8,6,3,4,2,6,7]
final = []
for element in lisin:
    if element not in final:
        final.append(element)  
print(lisin)
print(final)