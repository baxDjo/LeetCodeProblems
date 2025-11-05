import math

#Find the strictly greater power of 2, and subtract 1 from it.
class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2 ** math.ceil(math.log2(n + 1)) - 1



n = 10

solution = Solution()
