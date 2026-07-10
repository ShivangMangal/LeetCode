from typing import List
class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))
        vals = [x[0] for x in arr]
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid
        next_right = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and vals[r + 1] - vals[i] <= maxDiff:
                r += 1
            next_right[i] = r
        LOG = (n).bit_length()
        up = [next_right]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])
        def min_hops(left: int, right: int) -> int:
            if left == right:
                return 0
            if next_right[left] >= right:
                return 1
            cur = left
            ans = 0
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < right:
                    ans += 1 << k
                    cur = nxt
            return ans + 1
        res = []
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            pu, pv = pos[u], pos[v]
            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                res.append(-1)
            else:
                res.append(min_hops(pu, pv))
        return res