from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        exact = [0] * (n + 1)
        one = [0] * (n + 1)
        j0 = m - 1
        j1 = m - 1
        for i in range(n - 1, -1, -1):
            old_j0 = j0
            old_j1 = j1
            if old_j0 >= 0 and word1[i] == word2[old_j0]:
                j0 = old_j0 - 1
            if old_j1 >= 0 and word1[i] == word2[old_j1]:
                option1 = old_j1 - 1
            else:
                option1 = old_j1
            option2 = old_j0 - 1 if old_j0 >= 0 else old_j0
            j1 = min(option1, option2)
            exact[i] = m - 1 - j0
            one[i] = m - 1 - j1
        ans = []
        prev = -1
        mismatch_used = False
        for j in range(m):
            remaining = m - j - 1
            found = False
            for i in range(prev + 1, n):
                if word1[i] == word2[j]:
                    if one[i + 1] >= remaining:
                        ans.append(i)
                        prev = i
                        found = True
                        break
                elif not mismatch_used:
                    if exact[i + 1] >= remaining:
                        ans.append(i)
                        prev = i
                        mismatch_used = True
                        found = True
                        break
            if not found:
                return []
        return ans