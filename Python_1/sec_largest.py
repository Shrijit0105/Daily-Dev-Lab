
def second_largest(numbers):
    largest = None
    second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (
            second is None or number > second
        ):
            second = number

    return second


user_input = input("Enter a list of numbers separated by spaces: ")
result = second_largest(list(map(int, user_input.split())))


if result is not None:
    print("Second-largest number:", result)
else:
    print("No second-largest distinct number found.")
