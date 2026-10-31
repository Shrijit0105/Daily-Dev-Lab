def rotate(arr, k):

    n = len(arr)

    if n == 0:
        return arr

    k = k % n

    rotated_arr = arr[-k:] + arr[:-k]

    return rotated_arr


arr = [1, 2, 3, 4, 5]

user_input = input("Enter the number of positions to rotate the array: ")

result = rotate(arr, int(user_input))

print("Original array:", arr)
print("Rotated array:", result)