# Last updated: 8/29/2025, 6:48:04 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s)==Counter(t):
            return True
        return False
        