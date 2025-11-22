from typing import List, Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_nums = Counter(nums)
        result = 0
        for key, value in dict_nums.items():
            formula = value * (value - 1) // 2
            result += formula
        return result


sol = Solution()

nums = [1,2,3]
print(sol.numIdenticalPairs(nums))
