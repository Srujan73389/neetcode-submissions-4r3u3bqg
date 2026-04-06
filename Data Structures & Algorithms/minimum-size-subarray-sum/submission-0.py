class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,s,mini=0,0,float("inf")
        for r in range(len(nums)):
            s+=nums[r]
            while (s>=target):
                mini=min(mini,r-l+1)
                s-=nums[l]
                l+=1
        return 0 if mini==float('inf') else mini

        