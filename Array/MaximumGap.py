import heapq
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_difference = -float('inf')
        nums_sorted = sorted(nums)
        if len(nums_sorted) < 2:
            return 0
        for i in range(len(nums_sorted)-1):
            diff = nums_sorted[i+1] - nums_sorted[i]
            if diff > max_difference:
                max_difference = diff
        return max_difference


solution = Solution()

nums = [3,1]
print(solution.maximumGap(nums))
