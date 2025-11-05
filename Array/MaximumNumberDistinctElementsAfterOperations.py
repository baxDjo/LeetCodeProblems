from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        next_num_free = float('-inf')
        for num in nums:
            left = num - k
            right = num + k
            place = max(next_num_free, left)
            if place <= right:
                count += 1
                next_num_free = place + 1
        return count



solution = Solution()

nums = [4,4,4,4]
k = 1

print(solution.maxDistinctElements(nums, k))