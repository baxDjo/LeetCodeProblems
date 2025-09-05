class Solution:
    def removeDuplicates(self, s: str) -> str:
        stacks = [s[0]]
        for letter in s[1:]:
            if stacks and stacks[-1] == letter:
                stacks.pop()
            else:
                stacks.append(letter)
        return ''.join(stacks)


solution = Solution()
s = "azxxzy"
print(solution.removeDuplicates(s))