
def segregate_items(items):
    fruits = []
    vegetables = []
    unknown = []

    fruit_list = [
        "apple", "banana", "mango", "orange",
        "grapes", "watermelon", "papaya", "pineapple",
        "guava", "pear", "kiwi", "strawberry"
    ]

    vegetable_list = [
        "potato", "tomato", "onion", "carrot",
        "cabbage", "cauliflower", "spinach", "brinjal",
        "cucumber", "broccoli", "radish", "pumpkin"
    ]

    for item in items:
        item = item.strip().lower()

        if item in fruit_list:
            fruits.append(item.title())
        elif item in vegetable_list:
            vegetables.append(item.title())
        else:
            unknown.append(item.title())

    return fruits, vegetables, unknown


# Take input from the user
user_input = input("Enter fruits and vegetables separated by commas: ")

items = user_input.split(",")

fruits, vegetables, unknown = segregate_items(items)

print("\n--- Segregation Results ---")

print("\nFruits:")
print(", ".join(fruits) if fruits else "No fruits found.")

print("\nVegetables:")
print(", ".join(vegetables) if vegetables else "No vegetables found.")

if unknown:
    print("\nUnrecognized items:")
    print(", ".join(unknown))
