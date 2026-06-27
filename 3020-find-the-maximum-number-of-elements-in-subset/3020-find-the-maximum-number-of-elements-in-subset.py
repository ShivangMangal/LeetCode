from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = 1

        # Special handling for 1
        if 1 in cnt:
            if cnt[1] % 2:
                ans = cnt[1]
            else:
                ans = cnt[1] - 1

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                cur *= cur
                if cur > 10 ** 18:
                    break

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans