#  1. Write a Python program to convert a string to lowercase using a string method.
a = "THIS IS THE NORMAL STRING"
print(a.lower())

# 2. Given a string s = "Python Programming", write code to convert it to uppercase.
s = "Python Programming"
print(s.upper())


# 3. Write a Python program to find whether a string starts with a specific prefix (e.g., check if "Hello World!" starts with "Hello").
greet = "Hello World!"
print(greet.startswith("Hello"))


# 4. Given a string, use a method to check if it ends with a particular suffix (e.g., "world" in "Hello world!").
greet = "Hello world"
print(greet.endswith("world"))

# 5. Write a Python program to find the first occurrence of the substring "learn" in the string "Learn Python and learn programming.".
b = "Learn Python and learn programming."
print(b.find("learn"))

# 6. Given a string, remove all leading and trailing whitespaces using a suitable string method.
c = "      remove all leading and trailing whitespaces using a suitable string method     "
print(c.strip())

# 7. Replace all occurrences of "old" with "new" in the string "This is an old car. That is an old house.".
str = "This is an old car. That is an old house."
print(str.replace("old", "new"))

# 8. Write a Python program to split a string into a list of words using spaces as the delimiter.
d = "this is the simple statement"
print(d.split(" "))

# 9. Join a list of strings ["Python", "is", "fun"] into a single string with spaces between the words.

e = ["Python", "is", "fun"]
print(" ".join(e))


# 10. Write a program to count the occurrences of the word "apple" in the string "Apple is healthy. I like apple pie." (case-insensitive).
f = "Apple is healthy. I like apple pie."
f = f.lower()
array = f.split(" ")
count = 0
for i in array:
    if i == "apple":
        count += 1


print("here the count of apple is ", count)


# 11. Check if a given string is alphanumeric using a string method.
isAlphaNumeric = "abdbfnjdf"  # true
isAlphaNumeric = "abdbfnjdf43"  # false
print(isAlphaNumeric.isalpha())

# 12. Write a Python program to find all the characters in a string that are digits.
name = "abdullah123"
