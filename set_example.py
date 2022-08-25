#  Sets are unordered collection of items, with NO duplicate entries
#  used with curly brackets
# We cannot index/slice the items of the set
#  items are hashable like dict keys. so we can't put list in to sets
# if items in the 2 sets are equal then both of the sets will be equal
# but for tuples and lists the items and order should be equal for 2 tuples/lists to be equal
farm_animals = {'sheep', 'cow', 'hen', 'goat', 'horse'}

for animal in farm_animals:
    print(animal)  # execute this line of code multiple times, each execution shows diff result

farm_animals2 = {'horse', 'cow', 'sheep', 'goat', 'hen'}

if farm_animals2 == farm_animals:
    print("Two sets are equal")  # sets looking only for items not order
else:
    print("Sets are not equal")

#   How to create an empty set
#####################################################################################################
# numbers = {}  # takes as dictionary
# numbers = {*""} # takes as set but don't create a set in this way
numbers = set()  # best way to create an empty set
print(numbers, type(numbers))
numbers.add(1)
numbers.add("two")
numbers.add(2.5)
numbers.add('c')
print(numbers)
#  Remove duplicates from list
#######################################################################################################
data = ["blue", "red", "green", "blue", "green"]

print("After removing duplicates ...... ")
print(set(data))  # converts to set
print(sorted(set(data)))    # returns list
print(list(dict.fromkeys(data)))  # creates dictionary and convert to list using the keys in dictionary

# Remove items from set
##################################################################################################################
small_ints = set(range(21))
print(small_ints)
small_ints.discard(10)  # discard method to remove item from set
small_ints.remove(11)   # remove method to remove item from set
print(small_ints)
small_ints.discard(10)  # try again to remove already removed item
#  small_ints.remove(11)  # gets error while removing item
small_ints.pop()
print(small_ints)
small_ints.pop()
print(small_ints)
# 'update' method to add items from one set to another set
large_ints = {1000, 2000}
small_ints.update(large_ints)
print(small_ints)
small_ints.a