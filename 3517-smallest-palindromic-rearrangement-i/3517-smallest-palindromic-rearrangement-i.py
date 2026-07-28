from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        half = []
        mid = ""
        for ch in sorted(freq):
            half.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                mid = ch
        left = "".join(half)
        return left + mid + left[::-1]