from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        dict_s = Counter(s)
        max_freq_cons = 0
        max_freq_vowels = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for letter in set(s):
            if letter not in vowels:
                max_freq_cons = max(max_freq_cons, dict_s[letter])
            else:
                max_freq_vowels = max(max_freq_vowels, dict_s[letter])
        return max_freq_vowels + max_freq_cons

solution = Solution()

s = "successes"

print(solution.maxFreqSum(s))