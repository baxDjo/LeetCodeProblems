from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_nums = {}
        for idx, num in enumerate(nums):
            if num not in dict_nums:
                dict_nums[num] = idx
            else:
                distance = abs(dict_nums[num] - idx)
                if distance <= k:
                    return True
                else:
                    dict_nums[num] = idx
        return False


solution = Solution()

#nums = [99,99]
#k = 2

nums = [1,2,3,1,2,3]
k = 2
print(solution.containsNearbyDuplicate(nums, k))
