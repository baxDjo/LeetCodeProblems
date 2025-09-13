class Solution:
    def sortVowels(self, s: str) -> str:
        words = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        arr_vowels = [letter for letter in s if letter in vowels]
        arr_vowels_sorted = sorted(arr_vowels)
        arr_vowels_sorted.reverse()
        result = ''
        for letter in words:
            if letter in vowels:
                vowel = arr_vowels_sorted.pop()
                result += vowel
            else:
                result += letter
        print(words)
        print(arr_vowels_sorted)
        return result



solution = Solution()

s = "lEetcOde"

print(solution.sortVowels(s))