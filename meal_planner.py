from contents import pantry, recipes

# example
print(pantry)
print(recipes)
display_menu = {}
for index, key in enumerate(recipes):  # to get index/to do looping enumerate is used
    display_menu[str(index + 1)] = key  # creates new dict/transforms the keys from one dict to values of another dic
print("Please select the option to get the recipe >> \n")
for key, value in display_menu.items():  # to get both key and values, .items() is been used
    print(key, value)
chosen_menu = input()

menu_recipe = []

if chosen_menu in display_menu:
    chosen_value = display_menu[chosen_menu]
    if chosen_value in recipes:
        menu_recipe = recipes[chosen_value]
print(f"Find the recipe for {chosen_value}\n")
for index, item in enumerate(menu_recipe):
    print(index+1, item)
