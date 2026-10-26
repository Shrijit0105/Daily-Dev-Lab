
def move_zeros(numbers):
    position = 0

    # Move all non-zero values to the front
    for current in range(len(numbers)):
        if numbers[current] != 0:
            numbers[position], numbers[current] = (
                numbers[current],
                numbers[position]
            )
            position += 1

    return numbers


# Test cases
test_cases = [
    [0, 1, 0, 3, 12],
    [0, 0, 5],
    [1, 2, 3],
    [],
    [0, 0, 0],
    [-1, 0, 4, 0, -3]
]

for numbers in test_cases:
    original = numbers.copy()
    result = move_zeros(numbers)
    print(f"Input: {original} -> Output: {result}")
