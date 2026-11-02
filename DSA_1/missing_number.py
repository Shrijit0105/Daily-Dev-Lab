def find_missing_numbers(arr, n):
    num_set = set(arr)
    missing = []

    for i in range(1, n + 1):
        if i not in num_set:
            missing.append(i)

    return missing


# Test cases
arr1 = [1, 2, 4, 6, 7]
arr2 = [1, 2, 3, 4, 5]
arr3 = [2, 4, 6, 8]

print(find_missing_numbers(arr1, 7))  # [3, 5]
print(find_missing_numbers(arr2, 5))  # []
print(find_missing_numbers(arr3, 8))  # [1, 3, 5, 7]