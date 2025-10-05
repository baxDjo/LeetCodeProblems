from AliceBobPlayingFlowerGame import Solution


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        len_v1 = len(version1_list)
        len_v2 = len(version2_list)
        if len_v1 > len_v2:
            target = len_v1 - len_v2
            version2_list.extend(['0']*target)
        elif len_v1 < len_v2:
            target = len_v2 - len_v1
            version1_list.extend(['0']*target)
        while i < len(version1_list):
            if int(version1_list[i]) < int(version2_list[i]):
                return -1
            if int(version1_list[i]) > int(version2_list[i]):
                return 1
            i += 1
        return 0






sol = Solution()

version1 = "1.0"
version2 = "1.0.0.0"

print(sol.compareVersion(version1, version2))