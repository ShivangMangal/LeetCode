from typing import List
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)
        ans = (n - len(reserved)) * 2
        for seats in reserved.values():
            left = not any(seat in seats for seat in [2, 3, 4, 5])
            middle = not any(seat in seats for seat in [4, 5, 6, 7])
            right = not any(seat in seats for seat in [6, 7, 8, 9])
            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
        return ans