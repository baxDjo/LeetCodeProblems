from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text_split = text.split()
        print(text_split)
        for i in range (1, len(text_split)-1):
            print(text_split[i-1] , text_split[i], text_split[i+1])
            if text_split[i-1] == first and text_split[i] == second:
                result.append(text_split[i+1])
        return result



sol = Solution()

text = "alice is a good girl she is a good student"
first = "a"
second = "good"

print(sol.findOcurrences(text, first, second))