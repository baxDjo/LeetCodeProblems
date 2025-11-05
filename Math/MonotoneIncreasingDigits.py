from unicodedata import digit


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        stop = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] -= 1
                stop = i
        for i in range(stop, len(digits)):
            digits[i] = 9
        return int("".join(map(str, digits)))

    def isIncreasing(self, s: str) -> bool:
        return ''.join(sorted(s)) == s



n = 332

s = Solution()

print(s.monotoneIncreasingDigits(n))
