#LeetCode 225 – Implement Stack using Queues

"""There are two common approaches:
Using Two Queues
Using One Queue"""

"""Solution 1: Using Two Queues
Idea
push(x):
Put new element into q2.
Move all elements from q1 to q2.
Swap q1 and q2.
Now the newest element is always at the front of q1, so pop() becomes easy.
Example
Push 1
q1 = [1]
Push 2
q2 = [2]

Move q1 → q2

q2 = [2,1]

Swap

q1 = [2,1]
Top of stack = Front of queue = 2"""

"""Solution 2: Using One Queue
Idea
When pushing a new element:
Insert it at the back.
Rotate the queue so that the new element comes to the front.
This makes the queue behave exactly like a stack.
Example
Push 1
[1]
Push 2
Append:
[1,2]
Rotate once
[2,1]
Push 3
Append
[2,1,3]
Rotate twice
[1,3,2]
Rotate again
[3,2,1]
Now front is always the stack top."""

******************************************************************************************

#using 2 qeues

from collections import deque
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self) -> int:
        return self.q1.popleft()
    def top(self) -> int:
        return self.q1[0]
    def empty(self) -> bool:
        return len(self.q1) == 0

  ******************************************************************************************
# using single queue

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        # Rotate the queue
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
        
****************************************************************************************************
#implement queue using stack ... leetcode 232
"""it can be done by using two stacks"""

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output_stack.pop()

    def peek(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


****************************************************************************************************
#monotonic stack 
"""A Monotonic Stack is a stack in which the elements are always kept in a specific order:
Monotonic Increasing Stack: Elements are in increasing order (small → large).
Monotonic Decreasing Stack: Elements are in decreasing order (large → small).
It is mainly used to find:
Next Greater Element
Next Smaller Element
Previous Greater Element
Previous Smaller Element
Largest Rectangle in Histogram
Daily Temperatures
Stock Span
The time complexity is usually O(n) because each element is pushed and popped at most once."""

"""1. Monotonic Increasing Stack
Rule:
Before pushing the current element, remove all greater elements from the top.

while stack and stack[-1] > num:
    stack.pop()

stack.append(num)"""

"""2. Monotonic Decreasing Stack
Rule:
Before pushing the current element, remove all smaller elements.

while stack and stack[-1] < num:
    stack.pop()

stack.append(num)"""

#leetcode 496 next greater element
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        for num in nums2:
            while stack and num > stack[-1]:
                ans[stack.pop()] = num
            stack.append(num)
        return [ans.get(num, -1) for num in nums1]
