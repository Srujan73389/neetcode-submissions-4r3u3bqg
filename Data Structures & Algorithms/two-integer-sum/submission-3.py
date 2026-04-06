class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_mm={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hash_mm:
                return [hash_mm[diff],i]
            else:
                hash_mm[nums[i]]=i

        
        