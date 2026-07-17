#LINKEDLIST : LINKEDLIST LINEAR DATA STRUCTURE WHERE ELEMNETS CALLED NODES ARE CONNECTED USING POINTERS.
"""A Linked List is a non-contiguous data structure.
Nodes are not stored next to each other in memory.
Each node can be located anywhere in memory.
Nodes are connected through pointers."""

***********************************************************************************************

#CREATE AND TRAVERSE
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")

**************************************************************************************************


#using rec reverse linkedlist
def reverseList(self, head):
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

**************************************************************************************************

#INSERT AT BEGINNING
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
head = ListNode(20)
head.next = ListNode(30)

new_node = ListNode(10)
new_node.next = head
head = new_node
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

*************************************************************************************************

#INSERT AT END
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(10)
head.next = ListNode(20)

new_node = ListNode(30)

curr = head
while curr.next:
    curr = curr.next

curr.next = new_node

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

**************************************************************************************************
#leetcode 234 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        return lis == lis[::-1]

        #linked list method is also there where we can use slow and fast linked list concept

        """class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Compare both halves
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:  # Only need to check the second half length
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True"""
