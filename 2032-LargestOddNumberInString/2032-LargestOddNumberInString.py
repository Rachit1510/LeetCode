# Last updated: 8/29/2025, 6:47:46 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 == 1:
                return num[0:i+1]
        return ""