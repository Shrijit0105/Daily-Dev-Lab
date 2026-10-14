def palindrome(s):
  left=0
  right=len(s)-1

  while left < right:
     if s[left] != s[right]:
        return False
     left += 1
     right -= 1

  return True   


user_input = input("Enter a string: ")
result = palindrome(user_input)
if result:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')