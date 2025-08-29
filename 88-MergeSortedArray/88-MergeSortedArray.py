# Last updated: 8/29/2025, 6:48:22 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1  
        z = m + n - 1        

        while y >= 0: 
            if x >= 0 and nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
            z -= 1
