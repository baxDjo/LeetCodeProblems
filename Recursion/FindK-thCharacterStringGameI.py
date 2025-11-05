import string


class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        previous_word = "b"
        while len(word) <= k:
            word += previous_word
            for i in range(len(previous_word)):
                previous_word += chr(ord(previous_word[i]) + 1)
        result = word[k-1]
        return result


solution = Solution()

k = 5
print(solution.kthCharacter(k))

