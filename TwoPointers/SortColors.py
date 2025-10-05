from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        count_one = nums.count(1)
        count_two = nums.count(2)
        nums.clear()
        for _ in range(count_zero):
            nums.append(0)
        for _ in range(count_one):
            nums.append(1)
        for _ in range(count_two):
            nums.append(2)
        print(nums)


sol = Solution()

nums = [2,0,2,1,1,0]

print(sol.sortColors(nums))