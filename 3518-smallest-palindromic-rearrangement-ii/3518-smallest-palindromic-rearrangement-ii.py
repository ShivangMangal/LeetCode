from collections import Counter
from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        half = [0] * 26
        mid = ""
        for ch, cnt in freq.items():
            half[ord(ch) - 97] = cnt // 2
            if cnt % 2:
                mid = ch
        def multinomial(cnts):
            rem = sum(cnts)
            res = 1
            for c in cnts:
                if c:
                    res *= comb(rem, c)
                    rem -= c
            return res
        ways = multinomial(half)
        if ways < k:
            return ""
        total = sum(half)
        left = []
        while total:
            for i in range(26):
                if half[i] == 0:
                    continue
                newWays = ways * half[i] // total
                if k > newWays:
                    k -= newWays
                else:
                    left.append(chr(i + 97))
                    ways = newWays
                    half[i] -= 1
                    total -= 1
                    break
        left = "".join(left)
        return left + mid + left[::-1]