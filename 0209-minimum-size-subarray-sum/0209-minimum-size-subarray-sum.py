class Solution:
    def minSubArrayLen(self, target: int, arr: list[int]) -> int:
        n=len(arr)
        low=0
        
        min_len=float('inf')
        sum=0
        for high in range(n):
            sum+=arr[high]
            while(sum>=target):
                length=high-low+1
                min_len=min(min_len,length)
                sum-=arr[low]
                low+=1
        if (min_len==float('inf')) :
            return 0
        else:
            return min_len         


            



        