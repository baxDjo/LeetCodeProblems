from typing import List

from Matrix.LuckyNumbersMatrix import solution


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexTarget = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[indexTarget] , nums[i] = nums[i], nums[indexTarget]
                indexTarget += 1
        return indexTarget

solution = Solution()


nums = [3,2,2,3]
val = 3

print(solution.removeElement(nums, val))