import time

start = time.time()
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left, right = 2, num-1
        while left <= right:
            mid = left + (right-left)//2
            square = mid*mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

solution = Solution()
n = 16

end = time.time()
clock = str(end-start)

print(solution.isPerfectSquare(n))

print("time executed:",clock)