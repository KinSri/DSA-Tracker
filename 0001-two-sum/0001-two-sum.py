class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        hashmap={}
        for i in range(n):
            complement=target-nums[i]
            if complement in hashmap:
                return[i,hashmap[complement]]
            hashmap [nums[i]]=i  
        return []     
           

                
