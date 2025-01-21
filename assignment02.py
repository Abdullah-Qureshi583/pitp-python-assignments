# Q6 Write a Python program to calculate the electricity bill based on the following rates:

# For the first 100 units: $0.50 per unit
# For the next 100 units: $0.75 per unit
# Above 200 units: $1.20 per unit Calculate the total bill based on user input.


def calcElectricBill():
    unitsConsumed = float(input("Enter the number of units consumed: "))
    if unitsConsumed <= 100:
        bill = unitsConsumed * 0.50
        print("The electricity bill is $", bill)
    elif unitsConsumed <= 200:
        bill = (100 * 0.50) + ((unitsConsumed - 100) * 0.75)
        print("The electricity bill is $", bill)
    else:
        bill = (100 * 0.50) + (100 * 0.75) + ((unitsConsumed - 200) * 1.20)
        print(
            "You will be charged an additional ",
            bill - unitsConsumed * 0.50,
            " for the remaining units.",
        )
    return bill


# calcElectricBill()


# Q7 Write a Python program to check if a given number is divisible by 3, 5, both, or neither.
def isDivisibleBy3or5():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print(num, "is divisible by both 3 and 5.")
    elif num % 3 == 0 or num % 5 == 0:
        if num % 3 == 0:
            print(num, "is divisible by 3.")
        else:
            print(num, "is divisible by 5.")
    else:
        print(num, " is neither divisible by 3 nor  5.")


# isDivisibleBy3or5()


# Q8 Write a Python program to print all even numbers between 1 and 50.
def evenNum1To50():
    for num in range(2, 51, 2):
        print(num)


# evenNum1To50()

# Q9 Write a Python program to print the multiplication table for a number provided by the user.


def printMultiplicationTable():
    num = int(input("Which table do you want the multiplication of : "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# printMultiplicationTable()
