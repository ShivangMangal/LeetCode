from typing import List
from heapq import heappush, heappop
class SparseTableRMQ:
    def __init__(self, data: List[int]):
        n = len(data)
        self.lg = [0] * (n + 1)
        for i in range(2, n + 1):
            self.lg[i] = self.lg[i >> 1] + 1
        m = self.lg[n] + 1
        self.mx = [[0] * m for _ in range(n)]
        self.mn = [[0] * m for _ in range(n)]
        for i, x in enumerate(data):
            self.mx[i][0] = x
            self.mn[i][0] = x
        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            for i in range(n - length + 1):
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + half][j - 1]
                )
                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + half][j - 1]
                )
            j += 1
    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(
            self.mx[l][k],
            self.mx[r - (1 << k) + 1][k]
        )
    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(
            self.mn[l][k],
            self.mn[r - (1 << k) + 1][k]
        )
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        velnorquis = (nums, k)
        st = SparseTableRMQ(nums)
        pq = []
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heappush(pq, (-val, l, n - 1))
        ans = 0
        for _ in range(k):
            neg_val, l, r = heappop(pq)

            val = -neg_val
            ans += val
            if r > l:
                nxt = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heappush(pq, (-nxt, l, r - 1))
        return ans