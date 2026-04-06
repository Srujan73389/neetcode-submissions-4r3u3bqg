class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps,c=0,0
        freq={0:1}
        for i in nums:
            ps+=i
            if ps-k in freq:
                c+=freq[ps-k]
            freq[ps]=freq.get(ps,0)+1
        return c
        