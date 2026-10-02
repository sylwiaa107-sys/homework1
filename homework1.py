#0.1. IC1.1 -- Type Coercion Pitfall
# a = "12"
# b = "5"

# total = int(a) + int(b)
# print(total)
#
# #0.1. IC1.3 -- String Formatting With Constraints/ f-string
# #f-string / .upper / ,.2f miejsca po przecinku
#
# name = "anna"
# score = 1234.5678
# percent = 0.876
#
# f"{name.upper()}"
# print(f"{name.upper()}")
# print(f"{score:,.2f}")
# print(f"{name.upper()} {score:,.2f} {percent:.1%}")

#0.1. IC1.4 -- Boolean Trap / True / False (brak wartosci w nawiasach = false)

# print(bool("False"))
# print(0 == False, 1 == True, 2 == True)
# print(bool(0), bool(0.0), bool(""), bool([]), bool({}),
# bool(None))
# print(bool("False"), bool("0"), bool([0]), bool({0: 0}))

#0.1. IC1.5 -- Integer Division and Modulo - operator  // operator % reszta z dzielenia
#n = 0/ 11/ 12 /13/ 25/ 100

# n = 0
# full_boxes = n // 12
# leftovers = n % 12
# total_boxes = full_boxes + int(1)
# print(f"total boxes is {full_boxes}")
# print(f"leftovers is {leftovers}")
# print(f"total amount of boxes you need is {total_boxes}")
#
# n = 100
# full_boxes = n // 12
# leftovers = n % 12
# total_boxes = full_boxes + int(1)
# print(f"total boxes is {full_boxes}")
# print(f"total leftovers is {leftovers}")
# print(f"total amount of boxes you need is {total_boxes}")


#0.1. IC1.6 -- Operator Precedence Bug // operator and oba czynniki brane pod uwage //
#operatos or - jeden badz drugi

# price = 100
# is_member  = True
# has_coupon = False
# discount = 0.20 if (is_member or has_coupon) and price > 50 else 0
# print(discount)


# 0.1. IC1.8 -- Variable Swap Without Temporary // zmiana wartosci zmiennych bez zmiennych pomocniczych

# a  = 50
# b = 40
#
# a, b = b, a
# print(a)

#0.1. IC1.7 -- Reading From Input With Validation
# while True:
#     try:
#         temperature = float(input("Enter your temperature in Celsius: "))
#         break
#     except ValueError:
#          print("Invalid input - Please enter a numeric value")
#
# fahrenheit = temperature * 9 / 5 + 32
# f"{fahrenheit:.1f}"
# print(f"{fahrenheit:.1f}")



#0.1. IC1.9 -- Mini Calculator With Error Reporting


# while True:
#     try:
#         numb1 = float(input("Enter a number: "))
#         numb2 = float(input("Enter another number: "))
#         break
#     except ValueError:
#         print("Invalid input - Please enter a numeric value")
#
# operator = input("Enter a operator +, -, *, / : ")
#
# if operator not in ("+", "-", "*", "/"):
#     print("Invalid input")
#
# elif operator == "+":
#     result = numb1 + numb2
#     print(result)
#
# elif operator == "-":
#     result = numb1 - numb2
#     print(result)
#
# elif operator == "*":
#     result = numb1 * numb2
#     print(result)
#
# elif operator == "/":
#     if numb2 == 0:
#         print("You cannot divide by zero")
#     else:
#         result = numb1 / numb2
#         print(result)

#0.1. IC1.10 -- Lottery Number Drawer / modul random
# random.sample - losuje bez powtorzen // random.randint losuje z powtorzeniami
# sorted() - sortowanie rosnaco

import random

while True:
        count = int(input("How many numbers would you like to draw? "))
        max_value = int(input("What is max value? "))


        if count > 0 and max_value >= count:
            numbers = random.sample(range(1, max_value + 1), count)
            print(", ".join(map(str, sorted(numbers))))
        else:
            print("impossible to draw without duplicates")
            continue

        answer = input("Draw again? (y/n) ")
        if answer == "n":
            break
