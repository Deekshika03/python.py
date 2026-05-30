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


