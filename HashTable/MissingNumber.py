from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = list(range(len(nums)+1))
        for num in target:
            if num not in nums:
                return num



solution = Solution()
nums= [0, 1]
print(solution.missingNumber(nums))