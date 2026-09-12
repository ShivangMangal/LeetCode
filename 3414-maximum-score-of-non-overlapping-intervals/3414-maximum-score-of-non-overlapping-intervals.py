from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort()

        starts = [x[0] for x in arr]

        # Find the first interval with start > current right
        nxt = [
            bisect_right(starts, arr[i][1])
            for i in range(n)
        ]

        # dp[i][k] = (maximum weight, lexicographically smallest indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Option 1: skip
                best = dp[i + 1][k]

                # Option 2: take
                future_weight, future_indices = dp[nxt[i]][k - 1]

                candidate = (
                    arr[i][2] + future_weight,
                    tuple(sorted((arr[i][3],) + future_indices))
                )

                if candidate[0] > best[0] or (
                    candidate[0] == best[0]
                    and candidate[1] < best[1]
                ):
                    best = candidate

                dp[i][k] = best

        return list(dp[0][4][1])