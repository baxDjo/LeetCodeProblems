class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        nbOps = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            else:
                if i == 0 or s[i-1]=='1':
                    nbOps += ones
        return nbOps


solution = Solution()
s = "1001101"

print(solution.maxOperations(s))