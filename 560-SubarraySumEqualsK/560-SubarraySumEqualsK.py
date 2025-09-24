# Last updated: 9/24/2025, 6:43:04 PM
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        hashmap = {0: 1}

        for num in arr:
            prefix_sum += num 
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
        