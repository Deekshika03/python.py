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


