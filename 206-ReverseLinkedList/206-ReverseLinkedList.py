# Last updated: 8/29/2025, 6:48:07 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        if not head:
            return None
        else:
            while curr:
                temp_next=curr.next
                curr.next=prev
                prev=curr
                curr=temp_next
        return prev