from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        max_num = max(nums_sorted)
        min_num = min(nums_sorted)
        return max(0, max_num - min_num - 2*k)

