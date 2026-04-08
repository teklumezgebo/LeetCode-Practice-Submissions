# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # this is a two ptr solution.
        # using one ptr for the current node and ont ptr for the prev node
        prev, curr = None, head

        # iterate through the linked list moving each pointer forward
        while curr:
            # keep temp copy of the curr.next node as it will be changed
            # to prev
            tmp = curr.next
            # switch pointers
            curr.next = prev
            prev = curr
            curr = tmp

        return prev