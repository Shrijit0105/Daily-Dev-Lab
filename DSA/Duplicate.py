def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return sorted(duplicates)


user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

result = find_duplicates(numbers)

if result:
    print(f"Duplicate numbers: {result}")
else:
    print("No duplicate numbers found.")
