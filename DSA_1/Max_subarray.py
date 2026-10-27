
def maximum_subarray(numbers):
    if not numbers:
        return None

    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


test_cases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [-3, -2, -5],
    [5],
    [1, 2, 3, 4],
    [-2, -1, 0, -3],
    []
]

for numbers in test_cases:
    print(
        f"Input: {numbers} | "
        f"Maximum subarray sum: {maximum_subarray(numbers)}"
    )
