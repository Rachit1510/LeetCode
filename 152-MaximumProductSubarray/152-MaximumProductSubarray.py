# Last updated: 10/10/2025, 5:26:09 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max=1
        current_min=1
        max_product= float('-inf')

        for i in range(len(nums)):
            if nums[i]<0:
                current_max,current_min= current_min, current_max
            
            current_max= max(nums[i],current_max*nums[i])
            current_min= min(nums[i],current_min*nums[i])
        
            max_product= max(max_product,current_max)
        return max_product


        