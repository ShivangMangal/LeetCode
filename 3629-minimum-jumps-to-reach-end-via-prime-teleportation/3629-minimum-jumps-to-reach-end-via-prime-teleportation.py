from collections import defaultdict, deque
from math import isqrt
from typing import List
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return True
        maxv = max(nums)
        spf = list(range(maxv + 1))

        for i in range(2, isqrt(maxv) + 1):
            if spf[i] == i:
                for j in range(i * i, maxv + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        factor_map = defaultdict(list)
        for i, x in enumerate(nums):
            val = x
            seen = set()
            while val > 1:
                p = spf[val]
                if p not in seen:
                    factor_map[p].append(i)
                    seen.add(p)
                while val % p == 0:
                    val //= p
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        used_prime = set()
        while q:
            i = q.popleft()
            if i == n - 1:
                return dist[i]
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = dist[i] + 1
                    q.append(ni)
            x = nums[i]
            if is_prime(x) and x not in used_prime:
                for ni in factor_map[x]:
                    if dist[ni] == -1:
                        dist[ni] = dist[i] + 1
                        q.append(ni)
                used_prime.add(x)
        return -1