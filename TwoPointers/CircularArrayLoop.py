from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        isValid = False
        idx = 0
        for num in nums:
            if num == nums:
                idx = (idx + nums[idx]) % n
                isValid = True
        return isValid


solution = Solution()

nums = [2, -1, 1, 2, 2]

print(solution.circularArrayLoop(nums))