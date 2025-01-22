# 1)Write a function sum_of_multiples(n, x) that calculates the sum of all multiples of x up to n # Output: 30 (2 + 4 + 6 + 8 + 10)


def sum_of_multiples(n, x):
    conditions = True
    result = 0
    sumOfAll = 0
    while conditions:
        if result == n:
            conditions = False
        else:
            result += x
            sumOfAll += result
    print(sumOfAll)
    return sumOfAll


sum_of_multiples(10, 2)


# 2)Write a function is_palindrome(word) that checks whether a given word is a palindrome (a word that reads the same backward as forward).
# The function should return True or False.
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("radar"))  # Output: True
print(is_palindrome("python"))  # Output: False


# # 3)Write a function fibonacci_sequence(n) that generates the first n numbers in the Fibonacci sequence as a list.


# def fibonacci_sequence(n):
#     sequence = [0, 1]
#     print(sequence[-2])
#     for i in range(n):
#         sequence.append(sequence[-1] + sequence[-2])

#     print(sequence)


# fibonacci_sequence(6)  # Output: [0, 1, 1, 2, 3, 5]
