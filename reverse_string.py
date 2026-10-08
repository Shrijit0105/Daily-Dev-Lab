def rev_string(name):
    for i in range(len(name)-1, -1, -1):
        print(name[i], end="")
    print()  # for a new line after printing the reversed string

user_input = input("Enter a string to reverse: ")
result = rev_string(user_input)