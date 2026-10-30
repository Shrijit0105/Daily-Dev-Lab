# Add missing number algorithm and test cases
def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    arr_sum = sum(arr)  # Sum of the given array
    missing_number = total_sum - arr_sum  # The missing number
    return missing_number


# Test cases
# Test case 1: Missing number in the middle
test_case_1 = [1, 2, 4, 5]
print("Test case 1 - Missing number:", find_missing_number(test_case_1)) 




