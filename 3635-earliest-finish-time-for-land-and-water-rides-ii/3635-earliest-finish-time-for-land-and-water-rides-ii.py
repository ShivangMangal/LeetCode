from typing import List
from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x for x, _ in rides]
            n = len(rides)
            pref_min_d = [0] * n
            pref_min_d[0] = rides[0][1]
            for i in range(1, n):
                pref_min_d[i] = min(pref_min_d[i - 1], rides[i][1])
            suff_min_sd = [0] * n
            suff_min_sd[-1] = rides[-1][0] + rides[-1][1]
            for i in range(n - 2, -1, -1):
                suff_min_sd[i] = min(
                    suff_min_sd[i + 1],
                    rides[i][0] + rides[i][1]
                )
            return s, pref_min_d, suff_min_sd
        water_struct = build(waterStartTime, waterDuration)
        land_struct = build(landStartTime, landDuration)
        def best_finish_after(T, struct):
            starts, pref_min_d, suff_min_sd = struct
            n = len(starts)
            idx = bisect_right(starts, T) - 1
            ans = float('inf')
            if idx >= 0:
                ans = min(ans, T + pref_min_d[idx])
            if idx + 1 < n:
                ans = min(ans, suff_min_sd[idx + 1])
            return ans
        ans = float('inf')
        for s, d in zip(landStartTime, landDuration):
            end_land = s + d
            ans = min(ans, best_finish_after(end_land, water_struct))
        for s, d in zip(waterStartTime, waterDuration):
            end_water = s + d
            ans = min(ans, best_finish_after(end_water, land_struct))
        return ans