from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = [words[0]]
        for word in words[1:]:
            if stack and self.is_anagrams(stack[-1], word):
                pass
            else:
                stack.append(word)
        return stack

    def is_anagrams(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = Solution()
words = ["abba","baba","bbaa","cd","cd"]
print(solution.removeAnagrams(words))