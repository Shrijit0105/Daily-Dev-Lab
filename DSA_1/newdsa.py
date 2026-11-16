def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1


arr = [12, 45, 23, 67, 89, 34]

print(linear_search(arr, 67))  
print(linear_search(arr, 89))  
print(linear_search(arr, 100))  