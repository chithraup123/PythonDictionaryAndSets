vehicles = {
    'dream': 'Honda 250 T',
    'roadster': 'BMW R1100',
    'virago': 'Yamaha XV250'
}
# 2 methods to retrieve an item from dictionary
###################################################
my_vehicle1 = vehicles['virago']  # get one item from dictionary using 'indexing with key' method
print(my_vehicle1)
my_vehicle2 = vehicles.get('dream')  # 'get' method available in dictionary to get the item
print(my_vehicle2)

#  'indexing with key' returns error if key doesn't exist
#  'get' method returns 'None' if the key doesn't exist
#  better use get method if we are not sure about whether key exists, or not
#  but if we know that key exists, then use indexing with key since it is faster

# How to iterate over Dictionary
###############################################################################
print()
for key in vehicles:  # one way to iterate over dictionary
    print(key, vehicles[key], sep=",")
    # print(vehicle)

print()
print("Using .items() method of dictionary\n")
for key, value in vehicles.items():  # another way to iterate over dictionary using .items() method
    print(key, vehicles[key], sep=",")

#  How to add items to the dictionary
################################################################################
vehicles["toy"] = "glider"

print("Added new item\n")
for key, value in vehicles.items():
    print(key, value, sep=":")

# Dictionary maintains the insertion order/How to change the value in the dictionary
#################################################################################
vehicles['dream'] = "Honda 535 T"  # changed the value of dream key on second index since the key is repeated
print()
print("Added new item with existing key to check insertion order")
for key, value in vehicles.items():
    print(key, value, sep=":")

#  Removing an item from dictionary
######################################################################################
#  similar to deleting item from list using 'del' keyword
print("Removing an item from Vehicles\n")
del vehicles["virago"]
for key, value in vehicles.items():
    print(key, value, sep=":")
#  using 'pop' method

vehicles.pop("roadster")
print("\nRemove with pop method")
print(vehicles)

#  vehicles.pop("roadster")  # gets error when trying to remove the item which is not present in the dictionary

# if the item is not present then it returns the second arg we have given in pop method
result = vehicles.pop("roadster", "The item is not present")
print(result)
result = vehicles.pop("roadster", vehicles["dream"])
print(result)

#   for... in with dictionary
computer_parts = {1: "computer",
                  3: "monitor",
                  4: "keyboard",
                  2: "hard disk"}
current_choice = None

sorted_dict = sorted(computer_parts.items())  # sort computer_parts and gets list of tuples
print("After sorting..................\n")
print(dict(sorted_dict))

#  Prints the value in the dictionary as per user choice
# while current_choice !=0:
#     if current_choice in computer_parts:
#         part = computer_parts[current_choice]
#         print(f"The selected choice is {part}")
#     else:
#         print("Please select a valid option")
#         for key, value in computer_parts.items():
#             print(key, value, sep=":")
#     current_choice = int(input("Enter the choice >> "))


#  Stores the values of dictionary in to a list

# current_choice = None
# available_parts = []
# while current_choice != 0:
#     if current_choice in computer_parts:
#         chosen_part = computer_parts[current_choice]
#         if chosen_part in available_parts:
#             available_parts.remove(chosen_part)
#             print(f"\n{chosen_part} is removed")
#         available_parts.append(chosen_part)
#         print(f"\nAdded {chosen_part}")
#
#     print("Please select the option from the following >>")
#     for key, value in computer_parts.items():
#         print(key, value, sep=":")
#     print()
#     current_choice = int(input())
#
# print("The total parts available are")
# for index, part in enumerate(available_parts):
#     print(index, part, sep=",")
# current_choice = None
# available_parts = []
# while current_choice != 0:
#     if current_choice in computer_parts:
#         chosen_part = computer_parts[current_choice]
#         if chosen_part in available_parts:
#             available_parts.remove(chosen_part)
#             print(f"\n{chosen_part} is removed")
#         available_parts.append(chosen_part)
#         print(f"\nAdded {chosen_part}")
#
#     print("Please select the option from the following >>")
#     for key, value in computer_parts.items():
#         print(key, value, sep=":")
#     print()
#     current_choice = int(input())
#
# print("The total parts available are")
# for index, part in enumerate(available_parts):
#     print(index, part, sep=",")

# How to add item and remove item from dictionary
#################################################

available_parts = {1: "computer",
                   2: "monitor",
                   3: "keyboard",
                   4: "hard disk"}
index = 0
current_choice = None
computer_parts = {}
while current_choice != 0:
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            computer_parts.pop(current_choice)
        else:
            print("Adding item to dictionary")
            computer_parts[current_choice] = chosen_part
    print("Please select from the following option >> \n")
    for index, part in available_parts.items():
        print(index, part, sep=":")
    current_choice = int(input())
for key, value in computer_parts.items():
    print(key, value, sep=":")

iter(vehicles)