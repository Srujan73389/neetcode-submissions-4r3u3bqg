class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        has_m={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in has_m:
                return [has_m[diff]+1,i+1]
            has_m[n]=i

        