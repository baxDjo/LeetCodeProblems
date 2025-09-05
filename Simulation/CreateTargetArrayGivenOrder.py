from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            result.insert(index[i], nums[i])
            i += 1
        return result


solution = Solution()

nums = [0,1,2,3,4]
index = [0,1,2,2,1]


print(solution.createTargetArray(nums, index))