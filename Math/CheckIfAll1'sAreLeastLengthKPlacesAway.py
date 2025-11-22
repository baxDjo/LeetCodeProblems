from typing import List

#Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:
                for j in range(i+1, len(nums)):
                    target= (j - i - 1)
                    if nums[j] == nums[i] and target < k:
                        return False
                    elif nums[j] == nums[i] and target >= k:
                        break
        return True




solution = Solution()

nums = [1,0,0,0,1,0,0,1]
k = 2
print(solution.kLengthApart(nums, k))