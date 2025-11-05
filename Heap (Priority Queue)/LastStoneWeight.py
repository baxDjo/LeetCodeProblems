import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            first_greater = heapq.nlargest(1, stones)[0]
            index_idx1 = stones.index(first_greater)
            stones.remove(stones[index_idx1])
            second_greater = heapq.nlargest(1, stones)[0]
            index_idx2 = stones.index(second_greater)
            stones.remove(stones[index_idx2])
            if first_greater != second_greater:
                weight = abs(second_greater - first_greater)
                stones.append(weight)
        if  len(stones) == 1:
            return stones[0]
        else:
            return 0


sol = Solution()

stones = [2, 2]

print(sol.lastStoneWeight(stones))