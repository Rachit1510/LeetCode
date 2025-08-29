# Last updated: 8/29/2025, 6:48:24 PM
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes for less and greater lists
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        # terminate greater list
        greater.next = None
        # connect two lists
        less.next = greater_dummy.next
        
        return less_dummy.next
