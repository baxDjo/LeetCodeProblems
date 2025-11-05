from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum_even = self.add_even_numbers(nums)
        for query_idx in range(len(queries)):
            value, index = queries[query_idx]
            if nums[index] % 2 == 0:
                sum_even -= nums[index]
            nums[index] += value
            num_changed = nums[index]
            if num_changed % 2 == 0:
                sum_even += num_changed
            result.append(sum_even)
        return result


    def add_even_numbers(self, nums: List[int]) -> int:
        result  = [ num for num in nums if num % 2 == 0]
        return sum(result)

sol = Solution()

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(sol.sumEvenAfterQueries(nums, queries))
