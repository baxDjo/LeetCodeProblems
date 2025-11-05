from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for start1 in range(len(nums) - k + 1):
            first_window = nums[start1:start1 + k]

            for start2 in range(start1 + 1, len(nums) - k + 1):
                second_window = nums[start2:start2 + k]
                if len(first_window) == 1 or len(second_window) == 1:
                    return True

                if (self.is_strictly_increasing(first_window) and
                    self.is_strictly_increasing(second_window)):
                    if start2 - start1 == k:
                        return True
        return False

    def is_strictly_increasing(self, arr: List[int]) -> bool:
        return arr == sorted(arr) and len(arr) == len(set(arr))


sol = Solution()

nums = [2,5,7,8,9,2,3,4,3,1]
k = 3


print(sol.hasIncreasingSubarrays(nums, k))