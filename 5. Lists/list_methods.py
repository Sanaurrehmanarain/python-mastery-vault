x = [1, 5, 3, 9, 4, 8, 3, 9, "Max", 15.6]
y = ["tommy", 1, 15.6, [3, 2]]

x[2] # return the item at index 2
y[3] # return the item at index 3
x.insert(2, "tom") # inset 'tom' at index 2
x.remove("tom")
x.pop(5) # remove the item at index 5
x.clear() # clear all the items in the list without deleting the list
x.sort()
x.reverse()
del x # delete the list
x.append(10) # add 10 at the end of the list
z = x.copy() # copy to x list to the variable zfill
x.count(9) # count the total occurance of 9

# extend() method: Adds each element from an iterable (e.g., list, tuple) to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
# Result: [1, 2, 3, 4, 5, 6]

# += operator: Similar to extend(), but more concise.
my_list = [1, 2, 3]
my_list += [4, 5, 6]
# Result: [1, 2, 3, 4, 5, 6]

# append() in a loop: Adds items one by one.
my_list = [1, 2, 3]
for item in [4, 5, 6]:
    my_list.append(item)
# Result: [1, 2, 3, 4, 5, 6]

# pop()
lst = [1, 2, 3]
item = lst.pop(1)  # Removes and returns the element at index 1
print(item)  # Output: 2
print(lst)   # Output: [1, 3]

# remove()
lst = [1, 2, 3, 2]
lst.remove(2)  # Removes the first occurrence of 2
print(lst)  # Output: [1, 3, 2]

# del
lst = [1, 2, 3]
del lst[1]  # Deletes the element at index 1
print(lst)  # Output: [1, 3]

del lst     # Deletes the entire list
# print(lst)  # Raises a NameError because `lst` is deleted

"""
results = ["Mario", "Luigi"]

# Add item to the list, one at a time
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")

# To add more than one item to the list
results.append(["Toad", "Bowser", "Donkey Kong Jr."]) # This is wrong method, it will make a list within a list.

# To remove items.
results.remove(["Toad", "Bowser", "Donkey Kong Jr."])

# Add more than one item to the list in a proper manner.
results.extend(["Toad", "Bowser", "Donkey Kong Jr."])

print(results)
"""

results = ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']

# to remove an item
results.remove("Bowser")

# to insert an item with the index number
results.insert(1, "Bowser")

results.reverse() # It will reverse the items in the list.
print(results)