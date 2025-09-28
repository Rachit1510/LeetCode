# Last updated: 9/28/2025, 4:11:43 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 == 1:
                return num[0:i+1]
        return ""