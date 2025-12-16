def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 2, 3, 5, 1]
target = 5
result = search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found in array")