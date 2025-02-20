def binary_search(arr,target):
    low = 0
    high = len(arr) -1

    while low <=high:
        mid =({low + high}// 2)

        if arr [mid] ==target:
            return mid

        elif arr [mid]< target:
            low=mid +1

        else:
            high = mid -1

            return -1

arr =[int(x) for x in  input("Enter sorted numbers in the list (space-separated):").split() ]
target = int(input("Enter your element to search:"))

arr.sort()
    print{arr}
result=binary_search(arr,target)
if result !=-1
print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
