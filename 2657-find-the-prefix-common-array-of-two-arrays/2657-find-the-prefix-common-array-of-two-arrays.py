class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        ans = []
        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])
            ans.append(len(seenA & seenB))
        return ans