# Last updated: 10/10/2025, 5:26:02 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        current_sum=0
        min_len= float('inf')
        for right in range(len(nums)):
            current_sum+=nums[right]
        
            while current_sum>=target:
                min_len= min(min_len, (right-left)+1)
                current_sum-=nums[left]
                left+=1
    
        return 0 if min_len== float('inf') else min_len