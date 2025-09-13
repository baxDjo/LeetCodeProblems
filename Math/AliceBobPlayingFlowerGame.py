class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if m == n == 1:
            return 0
        return m*n//2


solution = Solution()

m = 3
n = 2

print(solution.flowerGame(m,n))