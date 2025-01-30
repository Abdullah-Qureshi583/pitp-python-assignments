# # 1)Problem: Create a list of numbers from 1 to 10. Use the .append() method to add the number 11 to the list,
# # and the .remove() method to remove the number 5.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # add the number 11 to the list
# nums.append(11)
# print(nums)
# # remove the number 5.
# nums.remove(5)
# print(nums)


# # 2)Problem: Given a list fruits = ['apple', 'banana', 'cherry'], use the .insert() method to add 'orange' at index 1.

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1, "orange")
# print(fruits)


# # 3)Problem: Use the .extend() method to merge two lists: list1 = [1, 2, 3] and list2 = [4, 5, 6].

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)


# # 4)Problem: Create a list of integers from 1 to 10 and use the .pop() method to remove the last element of the list.
# # Then print the removed element and the updated list.
# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# removedElement = integers.pop(-1)
# print(removedElement)


# # 5)Problem: Given a list names = ['John', 'Jane', 'Doe', 'Alice'], find the index of 'Doe' using the .index() method.

# names = ["John", "Jane", "Doe", "Alice"]
# doeIndex = names.index("Doe")
# print("The index of Doe is :", doeIndex)


# # 6)Problem: Given a list of numbers nums = [2, 3, 5, 7, 11, 13], remove all numbers greater than 10 using a loop and .remove() method.
# print("------------------")
# nums.remove(11)
# print(nums)


# nums = [2, 3, 5, 7, 11, 14, 13]
# numsCopy = nums.copy()
# for i in range(len(numsCopy)):
#     if numsCopy[i] > 10:
#         nums.remove(numsCopy[i])


# print(nums)

