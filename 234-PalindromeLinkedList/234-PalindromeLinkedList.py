# Last updated: 8/29/2025, 6:48:05 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        res=""

        while curr:
            res=res+str(curr.val)
            curr=curr.next
        
        if res==res[::-1]:
            return True
        return False