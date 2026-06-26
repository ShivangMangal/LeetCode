from typing import List
class Fenwick:
    def __init__(self,n):
        self.bit=[0]*(n+2)
    def update(self,i,delta):
        while i<len(self.bit):
            self.bit[i]+=delta
            i+=i&-i
    def query(self,i):
        s=0
        while i:
            s+=self.bit[i]
            i-=i&-i
        return s
class Solution:
    def countMajoritySubarrays(self,nums:List[int],target:int)->int:
        n=len(nums)
        offset=n+2
        bit=Fenwick(2*n+5)
        pref=0
        ans=0
        bit.update(offset,1)
        for x in nums:
            pref+=1 if x==target else -1
            idx=pref+offset
            ans+=bit.query(idx-1)
            bit.update(idx,1)
        return ans