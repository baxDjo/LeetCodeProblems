from typing import List, Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_sorted = [sorted(domino) for domino in dominoes]
        freqs = {}
        for domino in dominoes_sorted:
            if tuple(domino) in freqs:
                freqs[tuple(domino)] += 1
            else:
                freqs[tuple(domino)] = 1
        print(freqs)
        count = 0
        for key in freqs:
            calcul_pair = freqs[key] * (freqs[key] - 1) // 2
            count += calcul_pair
        return count

sol = Solution()

dominoes = [[1,2],[2,1],[3,4],[5,6]]

print(sol.numEquivDominoPairs(dominoes))