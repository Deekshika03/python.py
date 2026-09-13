""" 
in this order:
1. Stack implementation
        ↓
2. Queue implementation
        ↓
3. Reverse Stack
        ↓
4. Balanced Brackets
        ↓
5. Stack using 2 Queues
        ↓
6. Queue using 2 Stacks
        ↓
7. Next Greater Element
        ↓
8. Binary Numbers using Queue
        ↓
9. Stack filtering
        ↓
10. Histogram-style problems """


#Stack & Queue Practice Questions
#Q1. Implement Stack using a List
#Question:
#Implement a stack using a Python list. Create functions:
push(x)
pop()
peek()
isEmpty()
Solution:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())    # 30
print(s.pop())     # 30
print(s.pop())     # 20


#Q2. Implement Queue using a List
#Question:
#Implement a queue using a Python list with:
enqueue(x)
dequeue()
front()
isEmpty()
Solution:
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.pop(0)

    def front(self):
        if self.isEmpty():
            return -1
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.front())      # 10
print(q.dequeue())    # 10
print(q.dequeue())    # 20


#Q3. Reverse a Stack
#Question:
#Given a stack:
[10, 20, 30, 40]
reverse it so that:
[40, 30, 20, 10]
Solution:
stack = [10, 20, 30, 40]

reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(reversed_stack)
Output:
[40, 30, 20, 10]
Q4. Implement Stack using Two Queues
Question:
Create a stack using two queues.
Operations:
push()
pop()
Solution:
from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return -1
        return self.q1.popleft()


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())    # 30
print(s.pop())    # 20

"""Idea:
Stack → LIFO
Queue → FIFO
We rearrange the queue after every push() so that the newest element stays at the front.
"""
#Q5. Implement Queue using Two Stacks
#Question:
#Create a queue using two stacks.
"""Operations:
enqueue()
dequeue() """

Solution:
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2:
            return -1

        return self.s2.pop()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())    # 10
print(q.dequeue())    # 20

"""Idea:
s1 = [10, 20, 30]

transfer →

s2 = [30, 20, 10]

pop from s2 → 10
So FIFO behavior is achieved using stacks."""


#Q6. Check Balanced Brackets
#Question:
#Given:
"""  
"{[()]}"
check whether brackets are balanced.
"{[(])}"
should return False. """

#Solution:
def isBalanced(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in "([{":
            stack.append(ch)

        else:
            if not stack or stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


print(isBalanced("{[()]}"))   # True
print(isBalanced("{[(])}"))   # False


#Q7. Find Next Greater Element
#Question:
#For every element, find the first greater element on its right.
"""Input:  [4, 5, 2, 10, 8]

Output: [5, 10, 10, -1, -1]"""

#Solution:
def nextGreater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):

        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    return result


print(nextGreater([4, 5, 2, 10, 8]))
"""Output:
[5, 10, 10, -1, -1]"""

#Q8. Generate Binary Numbers using Queue
#Question:
#Using a queue, generate the first N binary numbers.
"""For:
N = 5
Output:
1 10 11 100 101"""

#Solution:
from collections import deque

def generateBinary(n):
    q = deque()
    q.append("1")

    for i in range(n):
        current = q.popleft()

        print(current, end=" ")

        q.append(current + "0")
        q.append(current + "1")


generateBinary(5)

"""Output:
1 10 11 100 101"""


#Q9. Remove All Even Elements from Stack
#Question:
#Given:
#[10, 15, 20, 25, 30]
#remove all even numbers.
#Output:
#[15, 25]
#Solution:
stack = [10, 15, 20, 25, 30]
temp = []

while stack:
    x = stack.pop()

    if x % 2 != 0:
        temp.append(x)

print(temp[::-1])


#Q10. Find Maximum Element in Stack
#Question:
#Given a stack, find the maximum element without using max().
"""[10, 50, 20, 40, 30]
Output:
50  """

#Solution:
stack = [10, 50, 20, 40, 30]

maximum = stack[0]

for x in stack:
    if x > maximum:
        maximum = x

print(maximum)
