from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        grid_row_sorted = [sorted(row) for row in grid]
        all_columns_grid_row_sorted = [[row[i] for row in grid_row_sorted] for i in range(len(grid_row_sorted[0]))]
        for row in all_columns_grid_row_sorted:
            result += max(row)
        return result



grid = [[1,2,4],[3,3,1]]

solution = Solution()

print(solution.deleteGreatestValue(grid))