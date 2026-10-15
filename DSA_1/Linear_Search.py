def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

target = int(input("Enter the number to search: "))
result = linear_search(numbers, target)

if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found.")