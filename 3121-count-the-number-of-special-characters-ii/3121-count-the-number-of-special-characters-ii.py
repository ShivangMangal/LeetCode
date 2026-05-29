class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            elif ch not in first_upper:
                first_upper[ch] = i

        ans = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in last_lower and c.upper() in first_upper:
                if last_lower[c] < first_upper[c.upper()]:
                    ans += 1

        return ans