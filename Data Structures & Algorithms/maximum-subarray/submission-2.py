class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cnt=0
        max_ct=float("-inf")
        for i in range(len(nums)):
            cnt=cnt+nums[i]
            max_ct=max(max_ct,cnt)
            if cnt<0:
                cnt=0
        return max_ct
        