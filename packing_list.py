#   This file contains an example to demonstrate the usage of 'discard' method available in the sets
####################################################################################################

travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # travelling by plane, remove restricted items
    # 1. discard
    #  can be used in a situation where we don't care about whether the item already exists earlier
    # We just need to delete the item if it is there
    for restricted_item in restricted_items:
        items.discard(restricted_item)

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)
