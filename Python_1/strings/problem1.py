# # Input:  "swiss"
# # Output: "w"

# def char_slice(str):
#     while len(str) > 1:
#         str = str[1:-1]
#     return str

# user_input = input("Enter a string: ")
# result = char_slice(user_input)
# print("Middle character(s):", result)




# Non-Repeating Character

def non_repeat(str):
    if len(str) == 0:
        return None
    else:
        for char in str:
            if str.count(char) == 1:
                return char
            elif str.count(char) > 1:
                continue  
          


while True:
        user_input = input("Enter a string: ")
        result = non_repeat(user_input)
        if result is not None:
            print("First non-repeating character:", result)
            break
        else:
            print("No non-repeating character found. Please try again.")     
