from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(N: int) -> int:
            if N < 0:
                return 0
            digits = list(map(int, str(N)))
            m = len(digits)
            @lru_cache(None)
            def dfs(pos: int, tight: bool, state: int, prev2: int, prev1: int):
                if pos == m:
                    return (1, 0)
                limit = digits[pos] if tight else 9
                total_count = 0
                total_wavy = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if state == 0:
                        if d == 0:
                            cnt, wav = dfs(pos + 1, ntight, 0, 0, 0)
                        else:
                            cnt, wav = dfs(pos + 1, ntight, 1, 0, d)
                    elif state == 1:
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)
                    else:  
                        local = 1 if (
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        ) else 0
                        cnt, wav = dfs(pos + 1, ntight, 2, prev1, d)
                        wav += local * cnt
                    total_count += cnt
                    total_wavy += wav
                return total_count, total_wavy
            return dfs(0, True, 0, 0, 0)[1]
        return solve(num2) - solve(num1 - 1)