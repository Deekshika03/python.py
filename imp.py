#reverse linkedlist
def reverse(head):
    prev = None

    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    return prev

#Factorial
def fact(n):
    if n<=1:
        return 1

    return n*fact(n-1)
  

#Remove Duplicates
def remove(nums):
    j = 0

    for i in range(1,len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j+1
  

#Valid Parentheses 
def valid(s):
    stack = []

    mp = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in mp.values():
            stack.append(ch)

        elif ch in mp:
            if not stack or stack.pop() != mp[ch]:
                return False

    return not stack

#leetcode problem : minimum climbing stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
