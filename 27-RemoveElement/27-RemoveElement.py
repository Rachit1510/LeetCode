# Last updated: 8/29/2025, 6:48:33 PM

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[k]=nums[i]
                k+=1
        return k