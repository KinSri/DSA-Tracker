class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest=nums[0]+nums[1]+nums[2]
        for i in  range(0,n-2):
            l,r=i+1,n-1
            while(l<r):
             curr_sum=nums[i]+nums[l]+nums[r]
             if (abs(curr_sum-target)<abs(closest-target)):
                closest=curr_sum
             if (curr_sum==target):
                return curr_sum
             elif (curr_sum>target):
                r-=1
             else:
                l+=1
        return closest        



        