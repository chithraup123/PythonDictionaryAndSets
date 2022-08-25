# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
# all_animals1 = farm_animals.union(wild_animals)
# print(all_animals1)
# all_animals2 = farm_animals | wild_animals
# print(all_animals2)

from prescription_data import *

adverse_set = set()
# loop each item from list and combine with adverse_Set
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for interaction in adverse_interactions:
#     # adverse_set = adverse_set.union(interaction)  # created a new set in each loop
#     adverse_set.update(interaction)  # update in the existing set, no need to create a new set everytime

# Update can take any no of sets , so no need to loop in a list of sets
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
adverse_set.update(*adverse_interactions)
print(sorted(adverse_set))
print(*sorted(adverse_set), sep="\n")  # here also * helped to take each one
# union of multiple sets using operator
num1 = {1, 2, 3}
num2 = {3, 4, 5}
num3 = {6, 7, 8}
res = num1 | num2 | num3
print(res)
