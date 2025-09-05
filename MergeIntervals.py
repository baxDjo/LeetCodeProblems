from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        result = []
        first_interval = intervals_sorted[0]
        if len(intervals_sorted) == 1:
            return [first_interval]
        for interval in intervals_sorted[1:]:
            if interval[0] <= first_interval[1]:
                first_interval = [first_interval[0], max(first_interval[1], interval[1])]
            else:
                result.append(first_interval)
                first_interval = interval
        result.append(first_interval)
        return result


solution = Solution()

intervals = [[1,4],[5,6]]
print(solution.merge(intervals))