# Last updated: 8/29/2025, 6:48:31 PM
class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:  
                return mid

            if target > nums[mid]:    
                l = mid + 1
            else:
                r = mid - 1
        return l   # l is the correct insert position
