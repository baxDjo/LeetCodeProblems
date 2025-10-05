
class Solution:
    def originalDigits(self, s: str) -> str:
        list_s = list(s)
        result = ''
        while 'z' or 'x' or 'w' or 'u' or 'g' in list_s:
            if 'z' in list_s:
                list_s.remove('z')
                list_s.remove('e')
                list_s.remove('r')
                list_s.remove('o')
                result += '0'
            if 'w' in list_s:
                list_s.remove('t')
                list_s.remove('w')
                list_s.remove('o')
                result += '2'
            if 'u' in list_s:
                list_s.remove('f')
                list_s.remove('o')
                list_s.remove('u')
                list_s.remove('r')
                result += '4'
            if  'x' in list_s:
                list_s.remove('s')
                list_s.remove('i')
                list_s.remove('x')
                result += '6'
            if 'g' in list_s:
                list_s.remove('e')
                list_s.remove('i')
                list_s.remove('g')
                list_s.remove('h')
                list_s.remove('t')
                result += '8'

            if 'o' in list_s:
                list_s.remove('o')
                list_s.remove('n')
                list_s.remove('e')
                result += '1'
            if 'h' in list_s:
                list_s.remove('t')
                list_s.remove('h')
                list_s.remove('r')
                list_s.remove('e')
                list_s.remove('e')
                result += '3'
            if 'f' in list_s:
                list_s.remove('f')
                list_s.remove('i')
                list_s.remove('v')
                list_s.remove('e')
                result += '5'
            if 'i' in list_s:
                list_s.remove('n')
                list_s.remove('i')
                list_s.remove('n')
                list_s.remove('e')
                result += '9'
            if not list_s:
                break
        return result

sol = Solution()

s = "owoztneoer"


print(sol.originalDigits(s))