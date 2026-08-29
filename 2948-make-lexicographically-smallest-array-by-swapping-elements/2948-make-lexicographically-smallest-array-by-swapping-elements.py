class Solution:
    def lexicographicallySmallestArray(self,nums:List[int],limit:int)->List[int]:
        n=len(nums)
        a=sorted((v,i) for i,v in enumerate(nums))
        res=nums[:]
        l=0
        while l<n:
            r=l
            while r+1<n and a[r+1][0]-a[r][0]<=limit:
                r+=1
            idx=sorted(a[k][1] for k in range(l,r+1))
            vals=[a[k][0] for k in range(l,r+1)]
            for i,v in zip(idx,vals):
                res[i]=v
            l=r+1
        return res