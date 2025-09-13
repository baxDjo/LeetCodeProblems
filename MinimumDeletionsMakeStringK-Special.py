from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        dict_word = Counter(word)
        if not word:
            return 0
        freq_min = min(dict_word, key=dict_word.get)
        freq_max = max(dict_word, key=dict_word.get)
        if dict_word[freq_max] - dict_word[freq_min] <= k:
            return 0
        set_word = set()
        for freq in dict_word.values():
            set_word.add(freq)
            set_word.add(max(0, freq - k))
        result = float('inf')
        for freq in set_word:
            cost = 0
            for freq_dict in dict_word.values():
                if freq_dict < freq:
                    cost = cost + freq_dict
                elif freq_dict > freq + k:
                    cost += freq_dict - (freq + k)
                else:
                    cost = cost + 0
            result = min(result, cost)
        return result



solution = Solution()

word = "aabcaba"
k = 0

print(solution.minimumDeletions(word, k))
