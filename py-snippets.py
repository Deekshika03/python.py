# current date and time
from datetime import datetime
now = datetime.now()
print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# contact book str
contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210"
}

name = input("Enter name: ")
if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print("Contact not found")


# stone , paper , scissor game 
    import random

choices = ["rock", "paper", "scissors"]
user = input("Rock, Paper or Scissors? ").lower()
comp = random.choice(choices)

print(f"Computer chose {comp}")

if user == comp:
    print("It's a tie!")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("You win!")
else:
    print("You lose!")


*******************************************************************************************
#array leetcode problem for single element
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans

*******************************************************
#pascal triangle
class Solution:
    def generate(self, numRows: int):
        triangle = []

        for row in range(numRows):
            new_row = [1] * (row + 1)

            for j in range(1, row):
                new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(new_row)

        return triangle
