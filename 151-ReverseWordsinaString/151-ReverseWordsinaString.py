# Last updated: 9/4/2025, 1:07:55 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        b=s.split()
        b.reverse()
        return(' '.join(b))