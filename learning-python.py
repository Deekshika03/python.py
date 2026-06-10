print("Hello, World!")

# basic_calculator.py
def add(a, b):
    return a + b #additon

def subtract(a, b):
    return a - b #substraction

def multiply(a, b):
    return a * b #multiplication

def divide(a, b):
    if b != 0:
        return a / b #division
    else:
        return "Error! Division by zero."

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation: +, -, *, /")
choice = input("Enter operation: ")

if choice == '+':
    print("Result:", add(num1, num2))
elif choice == '-':
    print("Result:", subtract(num1, num2))
elif choice == '*':
    print("Result:", multiply(num1, num2))
elif choice == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")


***********************************************************************
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
        #ladt word count

************************************************************************
#recursive
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


        #iterative 
        class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
