import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))


sol = Solution()

n = 5

print(sol.bulbSwitch(n))