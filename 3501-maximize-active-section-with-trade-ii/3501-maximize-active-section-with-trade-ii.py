import math
from typing import List

class SparseTable:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n == 0:
            return
        self.K = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.K)]
        
        for i in range(self.n):
            self.st[0][i] = nums[i]
            
        for i in range(1, self.K):
            j = 0
            while j + (1 << i) <= self.n:
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    def query(self, l: int, r: int) -> int:
        if l > r or self.n == 0:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Group contiguous '0' blocks
        zero_groups = []       # List of (start_index, length)
        zero_group_idx = [-1] * n
        
        for i, char in enumerate(s):
            if char == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
            zero_group_idx[i] = len(zero_groups) - 1

        num_zero_groups = len(zero_groups)
        
        # 2. Build adjacent sums array: adj_sums[i] = len(zero_groups[i]) + len(zero_groups[i+1])
        adj_sums = []
        for i in range(num_zero_groups - 1):
            adj_sums.append(zero_groups[i][1] + zero_groups[i + 1][1])
            
        st = SparseTable(adj_sums)
        
        ans = []
        for l, r in queries:
            g_l = zero_group_idx[l]
            g_r = zero_group_idx[r]
            
            # Base answer with no trades made
            max_active = total_ones
            
            # Calculate partial group lengths at boundary indices l and r
            left_len = 0
            if s[l] == '0':
                g_start, g_len = zero_groups[g_l]
                left_len = g_len - (l - g_start)
                
            right_len = 0
            if s[r] == '0':
                g_start, _ = zero_groups[g_r]
                right_len = r - g_start + 1
                
            # Case 1: l and r fall inside the same '0' group or adjacent '0' groups
            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                max_active = max(max_active, total_ones + left_len + right_len)
            
            # Case 2: Range Max Query for fully contained adjacent '0' group pairs
            start_adj = g_l + 1
            end_adj = (g_r - 1) if s[r] == '0' else g_r
            end_adj -= 1  # Map to adj_sums indices
            
            if start_adj <= end_adj:
                max_active = max(max_active, total_ones + st.query(start_adj, end_adj))
                
            # Case 3: Partial left group + complete next '0' group
            if s[l] == '0':
                target_next = g_r if s[r] == '1' else (g_r - 1)
                if g_l + 1 <= target_next:
                    max_active = max(max_active, total_ones + left_len + zero_groups[g_l + 1][1])
                    
            # Case 4: Partial right group + complete preceding '0' group
            if s[r] == '0' and g_l < g_r - 1:
                max_active = max(max_active, total_ones + right_len + zero_groups[g_r - 1][1])
                
            ans.append(max_active)
            
        return ans