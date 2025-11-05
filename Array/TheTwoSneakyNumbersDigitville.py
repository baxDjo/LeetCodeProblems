from typing import List, Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict_nums = Counter(nums)
        set_nums = set(nums)
        result = []
        for num in set_nums:
            if dict_nums[num] > 1:
                result.append(num)
        return result


solution = Solution()

nums = [7,1,5,4,3,4,6,0,9,5,8,2]

print(solution.getSneakyNumbers(nums))
