# Last updated: 8/29/2025, 6:47:50 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r= len(nums)-1
        res=[]

        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res.append(nums[l]**2)
                l=l+1
            else:
                res.append(nums[r]**2)
                r=r-1

        res.reverse()
        return res      

        