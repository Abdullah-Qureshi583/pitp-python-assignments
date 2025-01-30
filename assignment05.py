# Problem 1: Tuple Unpacking
# Create a tuple my_tuple containing three elements: (10, 20, 30). Unpack the tuple into three variables a, b, and c. Print the values of a, b, and c.
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)


# Problem 2: List Manipulation
# Create a list my_list with the following elements: [5, 10, 15, 20, 25]. Perform the following operations:
my_list = [5, 10, 15, 20, 25]


# Append the number 30 to the list.
print("original my_list ", my_list)
my_list.append(30)
print("append the 30 ", my_list)
# Remove the second element from the list.
my_list.pop(1)
print("remove the second element ", my_list)
# Insert the number 12 at the beginning of the list.
my_list.insert(0, 12)
print("Insert 12 at the beggining", my_list)
# Print the final list.
print("final my_list", my_list)


# Problem 3: Tuple Concatenation
# Create two tuples: tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6). Concatenate the two tuples into a new tuple called combined_tuple. Print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("combined_tuple", combined_tuple)  # Output: (1, 2, 3


# Problem 4: List Slicing
# Given the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract the first three elements.
extractedFirstThree = numbers[0:3]
print("extractedFirstThree", extractedFirstThree)

# Extract the last four elements.
extractedLastFour = numbers[-4:]
print("extractedLastFour", extractedLastFour)

# Extract every second element from the list.
extractedEverySecond = numbers[::2]
print("extractedEverySecond", extractedEverySecond)


# Problem 5: Tuple and List Conversion
# Create a tuple my_tuple = (7, 8, 9).
my_tuple = (7, 8, 9)
# Convert the tuple into a list called my_list.
my_list = list(my_tuple)

# Add the number 10 to the list.
my_list.append(10)

# Convert the list back into a tuple called new_tuple.
new_tuple = tuple(my_list)
# Print the final tuple.
print("new_tuple", new_tuple)
