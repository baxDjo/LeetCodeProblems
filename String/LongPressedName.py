from typing import Counter


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            prviousChar = name[i-1]
            if i < len(name) and  name[i] == typed[j]:
                i+=1
                j+=1
            else:
                if j != 0 and prviousChar == typed[j]:
                    j += 1
                else:
                    return False
        return i==len(name)


solution = Solution()

name = "saeed"
typed = "ssaaedd"

print(solution.isLongPressedName(name, typed))