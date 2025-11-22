from typing import List

# If original in nums Keep Multiplying Found Values by Two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        while original in nums:
            original *= 2
            if original not in nums:
                return original
        return original


solution = Solution()

nums = [5,3,6,1,12]
original = 3

print(solution.findFinalValue(nums, original))