# Last updated: 8/29/2025, 6:47:45 PM
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        sorted_nums= sorted(nums)
        if len(sorted_nums)>2:
            for i in range (len(sorted_nums)-1,-1,-1):
                if i!=0 and i!= len(sorted_nums)-1:
                    return sorted_nums[i]
        return -1
            
        