from typing import List

from Array.TheTwoSneakyNumbersDigitville import solution
#1 for each zero do if (sumLeft == sumRight ) result += 2
#2 for each zero do if abs(sumLeft - sumRight)>=1 result += 1

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sumLeft = sum(nums[:i])
                sumRight = sum(nums[i+1:])
                if sumLeft == sumRight:
                  result += 2
                elif abs(sumLeft - sumRight) == 1:
                    result += 1
        return result



solution =  Solution()

nums = [1,0,2,0,3]
print(solution.countValidSelections(nums))