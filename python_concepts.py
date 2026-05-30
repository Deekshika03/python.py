from collections import deque
#deque comes from Python's built-in collections module and allows you to add or remove elements from both ends efficiently.

# 1. Function
def greet(name):
    return f"Hello, {name}!"

print("FUNCTION:")
print(greet("Deekshika"))

# 2. List
print("\nLIST:")
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num, end=" ")


# 3. Dictionary
print("\nDICTIONARY:")
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BTech"
}

for key, value in student.items():
    print(f"{key}: {value}")



# 4. String Manipulation

print("\nSTRING:")
text = "Python"

print("Original:", text)
print("Uppercase:", text.upper())
print("Reverse:", text[::-1])


# 5. Recursion
print("\nRECURSION:")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 6. OOP
print("\nOOP:")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

s1 = Student("Aman", 21)
s1.display()


# 7. File Handling
print("\nFILE HANDLING:")

with open("sample.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning Python Concepts.")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# 8. Stack
print("\nSTACK:")

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

print("Popped:", stack.pop())

print("After Pop:", stack)



# 9. Queue

print("\nQUEUE:")

queue = deque()

queue.append(100)
queue.append(200)
queue.append(300)

print("Queue:", list(queue))

print("Dequeued:", queue.popleft())

print("After Dequeue:", list(queue))



# 10. Binary Tree
print("\nBINARY TREE:")

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder Traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

print("Inorder Traversal:")
inorder(root)

print("done!")
