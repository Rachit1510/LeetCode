# Last updated: 9/11/2025, 2:27:30 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z = 0
        o = 0
        t = 0
        for i in nums :
            if(i == 0) :
                z+=1
            if(i == 1) :
                o+=1
            if(i == 2) :
                t+=1 
        
        for i in range(0,len(nums)):
            if(z > 0) :
                nums[i] = 0
                z-=1
            else :
                if(o > 0) :
                    nums[i] = 1
                    o-=1
                else :
                    if(t > 0) :
                        nums[i] = 2
                        t-=1

        