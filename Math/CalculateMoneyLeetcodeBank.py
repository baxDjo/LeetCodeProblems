
class Solution:
    def totalMoney(self, n: int) -> int:
        n_weeks = n //7
        n_days = n%7;
        result = 28*n_weeks+ 7 * (n_weeks*(n_weeks-1)//2)
        result += n_days*n_weeks + n_days * (n_days + 1)//2
        return result

    def sum_num(self, num, start, end):
        res = 0
        for i in range(start, end+1):
            res += i
        return res



solution = Solution()

n = 20
#result = n / 2 * (2 * a + (n - 1) * d)
print(solution.totalMoney(n))

#print(solution.sum_num(7, 3, 8))
#print(28+35+33)

#n = 96 = 28 + 35 + 33