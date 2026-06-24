class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        base = [i for i in range(m)] 
        M = [[min(i, j) % MOD for j in range(m)] for i in range(m)]
        def mat_mul(A, B):
            nsz = len(A)
            C = [[0] * nsz for _ in range(nsz)]

            for i in range(nsz):
                Ai = A[i]
                Ci = C[i]

                for k in range(nsz):
                    a = Ai[k]
                    if a == 0:
                        continue

                    Bk = B[k]
                    for j in range(nsz):
                        Ci[j] = (Ci[j] + a * Bk[j]) % MOD
            return C
        def mat_vec_mul(A, v):
            nsz = len(A)
            res = [0] * nsz
            for i in range(nsz):
                s = 0
                row = A[i]
                for j in range(nsz):
                    s = (s + row[j] * v[j]) % MOD
                res[i] = s
            return res
        def power_apply(mat, exp, vec):
            while exp:
                if exp & 1:
                    vec = mat_vec_mul(mat, vec)

                mat = mat_mul(mat, mat)
                exp >>= 1
            return vec
        exp = n // 2 - 1
        vec = power_apply(M, exp, base)
        if n % 2 == 1:
            P = [
                [1 if j > m - 1 - i else 0 for j in range(m)]
                for i in range(m)
            ]
            vec = mat_vec_mul(P, vec)
        return (2 * sum(vec)) % MOD