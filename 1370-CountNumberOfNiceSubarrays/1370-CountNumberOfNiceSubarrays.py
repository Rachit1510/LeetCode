# Last updated: 10/12/2025, 2:00:01 PM
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        left = 0
        temp = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1
                temp=0

            while odd_count == k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1
                temp += 1

            count += temp

        return count
