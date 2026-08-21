from typing import List
from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            ans = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm // gcd(lcm, coins[i]) * coins[i]
                        if lcm > x:
                            valid = False
                            break
                if not valid:
                    continue
                multiples = x // lcm

                if bits % 2 == 1:
                    ans += multiples
                else:
                    ans -= multiples
            return ans
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left