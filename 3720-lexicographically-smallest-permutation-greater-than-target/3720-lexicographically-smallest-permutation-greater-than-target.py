class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = []
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')
            if cnt[t] > 0:
                cnt[t] -= 1
                ans.append(target[i])
                continue
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1
                    for x in range(26):
                        ans.extend([chr(x + ord('a'))] * cnt[x])
                    return ''.join(ans)
            while ans:
                prev = ord(ans.pop()) - ord('a')
                cnt[prev] += 1
                for c in range(prev + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1
                        for x in range(26):
                            ans.extend([chr(x + ord('a'))] * cnt[x])
                        return ''.join(ans)
            return ""
        while ans:
            prev = ord(ans.pop()) - ord('a')
            cnt[prev] += 1
            for c in range(prev + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1
                    for x in range(26):
                        ans.extend([chr(x + ord('a'))] * cnt[x])
                    return ''.join(ans)
        return ""