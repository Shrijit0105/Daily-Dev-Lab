def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


user_input = input("Enter a string: ")
result = count_vowels(user_input)

print("Number of vowels:", result)
