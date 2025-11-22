class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        isValid = True
        if num1 == 0 or num2 == 0:
            return 0
        while isValid:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
            if num1 == 0 or num2 == 0:
                isValid = False
        return count

sol = Solution()
num1 = 2
num2 = 3
print(sol.countOperations(num1, num2))