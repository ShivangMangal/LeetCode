class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        odd = 0
        middle = -1
        for i in range(26):
            if freq[i] % 2 == 1:
                odd += 1
                middle = i
        if odd > 1:
            return ""
        half = [x // 2 for x in freq]
        m = n // 2
        def build(left):
            left = ''.join(left)
            if n % 2:
                return left + chr(ord('a') + middle) + left[::-1]
            else:
                return left + left[::-1]
        cnt = half[:]
        left = []
        possible = True
        for i in range(m):
            c = ord(target[i]) - ord('a')
            if cnt[c] == 0:
                possible = False
                break
            left.append(chr(ord('a') + c))
            cnt[c] -= 1
        if possible:
            candidate = build(left)
            if candidate > target:
                return candidate
        for pivot in range(m - 1, -1, -1):
            cnt = half[:]
            left = []
            possible = True
            for i in range(pivot):
                c = ord(target[i]) - ord('a')
                if cnt[c] == 0:
                    possible = False
                    break
                left.append(chr(ord('a') + c))
                cnt[c] -= 1
            if not possible:
                continue
            target_char = ord(target[pivot]) - ord('a')
            bigger = -1
            for c in range(target_char + 1, 26):
                if cnt[c] > 0:
                    bigger = c
                    break
            if bigger == -1:
                continue
            left.append(chr(ord('a') + bigger))
            cnt[bigger] -= 1
            for c in range(26):
                while cnt[c] > 0:
                    left.append(chr(ord('a') + c))
                    cnt[c] -= 1
            return build(left)
        return ""