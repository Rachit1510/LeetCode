# Last updated: 8/29/2025, 6:47:53 PM
class Solution:
    def search(self, nums, target):
        N=len(nums)
        L=0
        R=N-1

        while L<=R:
            M=L+((R-L)//2)
            if target==nums[M]:
                return M
            elif target<nums[M]:
                R=M-1
            else:
                L=M+1
        return -1
        

