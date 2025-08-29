# Last updated: 8/29/2025, 6:48:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next== None:
            return None
        
        curr=head
        prev=None
        count=0

        while curr:
            count+=1
            curr=curr.next
        
        index_remove= count-n+1
        curr=head

        if index_remove==1:
            return head.next

        for i in range(index_remove-1):
            prev=curr
            curr=curr.next
        prev.next=curr.next

        return head



