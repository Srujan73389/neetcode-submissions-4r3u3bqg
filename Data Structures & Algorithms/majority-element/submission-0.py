class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c,res=0,0
        for i in nums:
            if c==0:
                res=i
            c+=(1 if i==res else -1)
        return res
        