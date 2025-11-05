from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        target = len(candyType) // 2
        candy_type_set = set(candyType)
        return min(len(candy_type_set), target)

solution = Solution()
candyType = [6,6,6,6]

print(solution.distributeCandies(candyType))