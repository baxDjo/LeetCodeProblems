from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2*arr[j]:
                    return True
                if arr[j]%2 == 0:
                    tmp = arr[j]//2
                    if arr[i] == arr[j]//2:
                        return True
        return False


solution = Solution()

arr = [7,1,14,11]
print(solution.checkIfExist(arr))