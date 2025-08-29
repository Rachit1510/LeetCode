# Last updated: 8/29/2025, 6:48:06 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen= set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False