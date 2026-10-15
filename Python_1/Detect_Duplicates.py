# def find_duplicates(lst):
#     lst=[]
#     left_search = 0
#     right_search = len(lst) - 1

#     while left_search != right_search:
#         if lst[left_search]==lst[right_search]:
#             lst.append(lst[left_search])
#             left_search+=1
#             right_search-=1
#         elif lst[left_search]<lst[right_search]:
#             left_search+=1
#         else:
#             right_search-=1
     

# def remove_duplicates(lst):
#     seen=set()
#     result=[]
#      for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# user_input = input("Enter a list of numbers separated by spaces: ")
# result = [int(x) for x in user_input.split()]
# duplicates = find_duplicates(result)
# removed_duplicates = remove_duplicates(duplicates)
# print("Duplicates found:", duplicates)



def find_duplicates(lst):
    duplicates = []
    left_search = 0

    while left_search < len(lst):
        right_search = left_search + 1

        while right_search < len(lst):
            if lst[left_search] == lst[right_search]:
                if lst[left_search] not in duplicates:
                    duplicates.append(lst[left_search])

            right_search += 1

        left_search += 1

    return duplicates


def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

duplicates = find_duplicates(numbers)
removed_duplicates = remove_duplicates(numbers)

print("Duplicates found:", duplicates)
print("List without duplicates:", removed_duplicates)

