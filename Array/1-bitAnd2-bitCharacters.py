from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
       index = 0
       while index < len(bits)-1:
           if bits[index] == 1:
               index += 2
           elif bits[index] == 0:
               index += 1
       return index == len(bits) - 1

solution = Solution()
bits = [1,0,0]

print(solution.isOneBitCharacter(bits))


