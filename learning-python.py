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


****************************************************************************
#find the duplicate number in array {leet code 287}
    class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            pos=abs(num)
            if nums[pos]<0:
                return pos
            nums[pos]= -nums[pos]    

"""explaination about code: The Core Concept: "Flagging" Visited ElementsThe code uses the
array itself as a checklist. When it encounters a number, it treats that number as a destination index 
and goes to that index to "flag" it by turning whatever number is sitting there into a negative value.
If it ever lands on an index that is already negative, it means another number pointed to this exact same spot earlier. 
That spot is the duplicate!

Step-by-Step Execution TraceLet's watch the loop run on nums = [1, 3, 4, 2, 2]:
Iteration 1: num = 1pos = abs(1) = 1Check nums[1]: It is 3 (positive, meaning index 1 hasn't been visited yet).
Flag it: Turn nums[1] negative $\rightarrow$ nums[1] = -3Array status: [1, -3, 4, 2, 2]
Iteration 2: num = -3pos = abs(-3) = 3 (Taking the absolute value is crucial here so we don't look up a negative index!)Check nums[3]: It is 2 (positive, index 3 is unvisited).
Flag it: Turn nums[3] negative $\rightarrow$ nums[3] = -2Array status: [1, -3, 4, -2, 2]
Iteration 3: num = 4pos = abs(4) = 4Check nums[4]: It is 2 (positive, index 4 is unvisited).Flag it: Turn nums[4] negative $\rightarrow$ nums[4] = -2Array status: [1, -3, 4, -2, -2]
Iteration 4: num = -2pos = abs(-2) = 2Check nums[2]: It is 4 (positive, index 2 is unvisited).Flag it: Turn nums[2] negative $\rightarrow$ nums[2] = -4Array status: [1, -3, -4, -2, -2]
Iteration 5: num = -2pos = abs(-2) = 2Check nums[2]: Look at the array status above. nums[2] is currently -4!Because nums[2] < 0, 
 the if condition triggers:Python
 if nums[pos] < 0:
    return pos
Result: The code immediately stops and returns pos (which is 2).

Why return pos and not return num?
This is because pos represents the index location where the collision occurred. 
Because the values within the array act as pointers mapping directly to those indices, the conflicting index is the duplicate number itself."""
