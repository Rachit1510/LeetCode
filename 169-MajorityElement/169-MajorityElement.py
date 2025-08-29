# Last updated: 8/29/2025, 6:48:10 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n//2]


        