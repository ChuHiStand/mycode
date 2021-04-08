#!/usr/bin/env python3

# for x in range(1,101):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)

# List comprehension #1
# fiz = ['FizzBuzz' if number%15==0 else 'Fiz' if number%3==0 else 'Buzz' if number%5==0 else number for number in range(
#     1, 101)]
# print(fiz)

# List comprehension #2
fiz2 = ["fizz"*(not number%3) + "Buzz"*(not number%5) or number for number in range(1, 101)]
print(fiz2)
