'''
Project Name: Fibonacci Generator

Author: Thisitha Wickramarachchi

Description: This program takes user input to determine how many Fibonacci numbers to 
generate and then provides the corresponding output.
'''

def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

nums = int(input("Number of fibonacci numbers you want to generate: "))

fib = fibonacci()
for _ in range(nums):
    print(next(fib), end=" ")

print("\n")