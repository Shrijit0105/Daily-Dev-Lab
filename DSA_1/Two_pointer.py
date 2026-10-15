def two_pointer_func(numbers,target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


user_input = input("Enter a list of numbers separated by spaces: ")
result = two_pointer_func(list(map(int, user_input.split())), int(input("Enter the target sum: ")))
if result:
    print(f'The indices of the two numbers that add up to the target are: {result}')
else:
    print("No two numbers add up to the target.")



