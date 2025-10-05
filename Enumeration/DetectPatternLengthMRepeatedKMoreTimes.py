from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = 1
        for i in range(len(arr)):
            pattern = arr[i:i+m]
            for j in range(i+2, len(arr)):
                patternTarget = arr[j:j+m]
                if pattern == patternTarget:
                    count += 1
                else:
                    count = 0
            if count >= k:
                return True
            count = 0
        return False



s = Solution()
arr = [1,2,1,2,1,1,1,3]
m = 2
k = 2
print(s.containsPattern(arr, m, k))