import numpy as np
array2=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print ("2-D Array:")
print(array2)
print ("\nElement at (1,2):", array2[1,2])
print("First row:", array2[0])

array2[0,1]=99
print("\nModified Array")
print(array2)

print("\nElements in 2-D Array:")
for row in array2:
    for element in row:
        print(element, end=' ')
    print()
