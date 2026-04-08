# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer

        prev, curr =  None, head

        while curr:
            ## create copy of curr's next pointer
            temp = curr.next
            # set the current.next pointer to prev 
            curr.next = prev
            # set prev to curr to move it forward
            prev = curr
            # set curr to the copy of the last curr's next pointer
            curr = temp
        # curr should be null when it reaches the end and prev should be the head of the list
        return prev