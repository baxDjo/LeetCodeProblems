from itertools import dropwhile


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) == 1 and k == 1:
            return '0'
        for digit in num:
            while stack and stack[-1] > int(digit) and k > 0:
                stack.pop()
                k -= 1
            stack.append(int(digit))
        if len(stack)==1:
            return str(stack[0])
        if k > 0:
            stack = stack[:-k]
        stack = list(dropwhile(lambda x: x == 0, stack))
        if not stack:
            return '0'
        stack = [str(i) for i in stack]
        return ''.join(stack)


solution = Solution()

num = "21"
k = 1
print(solution.removeKdigits(num, k))


