# Last updated: 8/29/2025, 6:48:19 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(ch.lower() for ch in s if ch.isalnum())
        l=0
        r=len(filtered)-1
        while l<r and filtered[l]==filtered[r]:
            l+=1
            r-=1
        if l>=r:
            return True
        return False            