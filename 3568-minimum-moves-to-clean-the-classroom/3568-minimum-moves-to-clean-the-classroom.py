from typing import List
from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        start = None
        litter = {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)
        k = len(litter)
        if k == 0:
            return 0
        full_mask = (1 << k) - 1
        q = deque()
        sr, sc = start
        q.append((sr, sc, energy, 0, 0))
        best = {(sr, sc, 0): energy}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, e, mask, moves = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                if e == 0:
                    continue
                ne = e - 1
                nmask = mask
                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]
                if classroom[nr][nc] == 'R':
                    ne = energy
                nmoves = moves + 1
                if nmask == full_mask:
                    return nmoves
                state = (nr, nc, nmask)
                if state in best and best[state] >= ne:
                    continue
                best[state] = ne
                q.append((nr, nc, ne, nmask, nmoves))
        return -1