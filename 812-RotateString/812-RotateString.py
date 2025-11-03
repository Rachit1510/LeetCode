# Last updated: 11/3/2025, 9:24:54 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        
        combined_str= s+s
        if goal in combined_str:
            return True
        
        return False
        