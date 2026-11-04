
def move_zeros(arr):

    position = 0

    for i in range(len(arr)):

        if arr[i] != 0:

            arr[position], arr[i] = arr[i], arr[position]

            position += 1

    return arr


# Test cases
arr1 = [0, 1, 0, 3, 12]
arr2 = [0, 0, 1, 2, 3]
arr3 = [1, 2, 3, 4]
arr4 = [0, 0, 0, 0]

print(move_zeros(arr1))
print(move_zeros(arr2))
print(move_zeros(arr3))
print(move_zeros(arr4))
