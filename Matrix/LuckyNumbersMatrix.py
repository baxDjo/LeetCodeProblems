from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        targetNumber = 0
        list_cols = list(zip(*matrix))
        for row in matrix:
            result.append(min(row))
        for col in list_cols:
            result.append(max(col))
        for num in result:
            if result.count(num) > 1:
                targetNumber = num
                break
        if targetNumber == 0:
            return []
        return [targetNumber]



solution = Solution()


matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(solution.luckyNumbers(matrix))