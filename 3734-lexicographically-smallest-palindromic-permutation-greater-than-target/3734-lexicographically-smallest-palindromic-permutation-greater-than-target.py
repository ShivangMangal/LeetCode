class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Check if s can form a palindrome
        odd = 0
        middle = -1

        for i in range(26):
            if freq[i] % 2 == 1:
                odd += 1
                middle = i

        if odd > 1:
            return ""

        # Characters available in the left half
        half = [x // 2 for x in freq]
        m = n // 2

        # Build palindrome from left half
        def build(left):
            left = ''.join(left)

            if n % 2:
                return left + chr(ord('a') + middle) + left[::-1]
            else:
                return left + left[::-1]

        # ---------------------------------------------------------
        # 1. Try to make the left half exactly equal to target[:m]
        # ---------------------------------------------------------

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

            # This handles cases like:
            # s = "bb", target = "ba"
            #
            # left = "b"
            # palindrome = "bb"
            # "bb" > "ba"
            if candidate > target:
                return candidate

        # ---------------------------------------------------------
        # 2. Find the smallest left half strictly greater than
        #    target[:m]
        # ---------------------------------------------------------

        # Try the rightmost possible position as the pivot.
        # Changing a later position gives a smaller answer.
        for pivot in range(m - 1, -1, -1):

            cnt = half[:]
            left = []

            # Match target prefix before pivot
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

            # At pivot, choose the smallest character
            # strictly greater than target[pivot]
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

            # Fill the remaining positions with the
            # smallest possible characters.
            for c in range(26):
                while cnt[c] > 0:
                    left.append(chr(ord('a') + c))
                    cnt[c] -= 1

            return build(left)

        return ""