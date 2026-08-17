def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    return binary_search(arr, mid + 1, high, target)

arr = [2, 5, 8, 10, 15, 20]
print(binary_search(arr, 0, len(arr)-1, 15))