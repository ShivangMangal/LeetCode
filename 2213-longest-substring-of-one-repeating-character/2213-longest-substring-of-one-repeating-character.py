class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a
            left_char, _, pref_a, suff_a, best_a, len_a = a
            _, right_char, pref_b, suff_b, best_b, len_b = b
            pref = pref_a
            suff = suff_b
            best = max(best_a, best_b)
            if a[1] == b[0]:
                if pref_a == len_a:
                    pref = len_a + pref_b
                if suff_b == len_b:
                    suff = len_b + suff_a
                best = max(best, suff_a + pref_b)
            return (left_char, right_char, pref, suff, best, len_a + len_b)
        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        build(1, 0, n - 1)
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])  
        return ans