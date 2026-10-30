# def water(current_state):
    
#     def change_state(water_state):
#             if water_state == "solid":
#                 print("Water is in solid state.")
#             elif water_state == "liquid":
#                 print("Water is in liquid state.")
#             elif water_state == "gas":
#                 print("Water is in gas state.")
#             else:
#                 print("Water is changing its state.")         

#   print("Current state -> ", water_state)

#     return change_state(water_state)


# user_input = input("Enter the state of water (solid, liquid, gas): ").strip().lower()
# result = water(user_input)    


def water(current_state):

    def change_state(water_state):

        if water_state == "solid":
            print("Water is in solid state.")

        elif water_state == "liquid":
            print("Water is in liquid state.")

        elif water_state == "gas":
            print("Water is in gas state.")

    while current_state not in ["solid", "liquid", "gas"]:
        print("Invalid state! Please try again.")
        current_state = input(
            "Enter the state of water (solid, liquid, gas): "
        ).strip().lower()

    print("Current state ->", current_state)

    return change_state(current_state)


user_input = input(
    "Enter the state of water (solid, liquid, gas): "
).strip().lower()

result = water(user_input)