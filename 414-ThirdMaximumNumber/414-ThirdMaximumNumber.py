# Last updated: 8/29/2025, 6:48:02 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums= list(set(nums))
        sorted_nums= sorted(unique_nums)
        for i in range(len(sorted_nums)-1,-1,-1):
            if len(sorted_nums)>=3:
                return sorted_nums[-3]
        return sorted_nums[-1] 
            

            
        