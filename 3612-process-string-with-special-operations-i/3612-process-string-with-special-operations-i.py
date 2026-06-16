class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for ch in s:
            if 'a' <= ch <= 'z':
                result += ch
            elif ch == '*':
                result = result[:-1]
            elif ch == '#':
                result += result
            else:  
                result = result[::-1]
        return result