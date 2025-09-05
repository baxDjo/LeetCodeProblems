from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        idx_even = 0
        idx_odd = 1
        result = [0]*len(nums)
        for num in nums:
            if num % 2 == 0:
                result[idx_even] = num
                idx_even += 2
            else:
                result[idx_odd] = num
                idx_odd += 2
        return result


solution = Solution()

nums = [2,3]

print(solution.sortArrayByParityII(nums))
