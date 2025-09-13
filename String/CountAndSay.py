from Array.FindScoreAllPrefixesArray import solution


class Solution:
    def countAndSay(self, n: int) -> str:
        count = 1
        result = '1'
        next_term = ''
        if n == 1:
            return '1'
        for i in range(1, n):
            j  = i
            while j < n:
                k = j
                while k < len(result) and result[k] == result[j]:
                    sizeGroup = k - j
                    next_term = sizeGroup + result[j]
                    j = k
                



        return result


solution = Solution()

n = 4
print(solution.countAndSay(n))