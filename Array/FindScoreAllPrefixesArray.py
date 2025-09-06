from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        score = 0
        result = []
        maxValue = -float('inf')
        for i in range(len(nums)):
            if nums[i] > maxValue:
                maxValue = nums[i]
            score += nums[i] + maxValue
            result.append(score)
        return result


solution = Solution()

nums = [2,3,7,5,10]

print(solution.findPrefixScore(nums))