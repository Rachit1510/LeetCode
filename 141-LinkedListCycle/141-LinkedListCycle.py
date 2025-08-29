# Last updated: 8/29/2025, 6:48:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True
            
        return False