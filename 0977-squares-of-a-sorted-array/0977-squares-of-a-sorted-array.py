class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n
        id=n-1
        i=0
        j=n-1
        while(i<=j):
            x=nums[i]**2
            y=nums[j]**2
            if(x>=y):
                res[id]=x
                i=i+1
                id=id-1
            else:
                res[id]=y
                id=id-1
                j=j-1    
        return res



    
        