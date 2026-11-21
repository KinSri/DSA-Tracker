class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cs=0
        ms=float("-inf")
        n=len(nums)
        for i in range(n):
            cs+=nums[i]
            ms=max(cs,ms)
            if cs<0:
                cs=0
            
        return ms


