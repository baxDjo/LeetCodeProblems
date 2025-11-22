class Solution:
    def maximum69Number(self, num: int) -> int:
        num_list = [int(digit) for digit in str(num)]
        for i, d in enumerate(num_list):
            if num_list[i] == 6:
                num_list[i] = 9
                break
        result = ''.join(map(str, num_list))
        return int(result)

solution = Solution()

num = 9669
print(solution.maximum69Number(num))