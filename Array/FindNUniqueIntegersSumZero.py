from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, n):
            result.append(i)
        negativeSum = -sum(result)
        result.append(negativeSum)
        return result


solution = Solution()

n = 5
print(solution.sumZero(n))