import time
from binary_search_tree import BinarySearchTree
# Remember when you run this file you haev to run from command line and dont use vs code extension use "python {file name} :)"
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# O(n**2)
# runtime: 7.156205892562866 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# o(n)
# using dictianary (cant use Dict)
# Run time of 0.00498652458190918 seconds
# cache = {}
# for name_1 in names_1:
#     cache[name_1] = name_1

# for name_2 in names_2:
#     if name_2 in cache:
#         duplicates.append(name_2)

# 0(n log n)
# runtime: 0.14558696746826172 seconds
# using binary search tree


bst = BinarySearchTree(names_1[0])
for count, name_1 in enumerate(names_1):
    if count == 0:
        continue
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
