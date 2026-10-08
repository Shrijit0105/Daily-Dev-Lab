# def rev_string(name):
#     for i in range(len(name)-1, -1, -1):
#         print(name[i], end="")
#     print()  # for a new line after printing the reversed string

# user_input = input("Enter a string to reverse: ")
# result = rev_string(user_input)


# Two pointer approach to reverse a string
def reverse_string_two_pointer(s):
    # Convert the string to a list to allow modification
    str_list = list(s)
    left, right = 0, len(str_list) - 1

    while left < right:
        # Swap the characters at left and right pointers
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    return ''.join(str_list)

user_input = input("Enter a string to reverse: ")
result = reverse_string_two_pointer(user_input)    
print("Reversed string:", result)