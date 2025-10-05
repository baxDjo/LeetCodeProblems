from typing import List, Counter


class Solution:
    def compress(self, chars: List[str]) -> int:
        reader = 0
        writer = 0
        while reader < len(chars):
            currentChar = chars[reader]
            start = reader
            while reader < len(chars) and chars[reader] == currentChar:
                reader += 1
            len_group = reader - start
            chars[writer] = currentChar
            writer += 1
            if len_group > 1:
                for digit in str(len_group):
                    chars[writer] = digit
                    writer += 1
        return writer


sol = Solution()

chars = ["a","a","b","b","c","c","c"]

print(sol.compress(chars))