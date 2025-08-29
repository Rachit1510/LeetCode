# Last updated: 8/29/2025, 6:48:20 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result