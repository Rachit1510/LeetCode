# Last updated: 8/29/2025, 6:48:03 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        total= n*(n+1)//2
        return total-sum(nums)
        