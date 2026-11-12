class Solution:

    def sortColors(self, num: list[int]) -> None:
       n=len(num) 
       low=0
       mid=0
       high=n-1
       while(mid<=high):
        if num[mid]==0:
            num[mid],num[low]=num[low],num[mid]
            mid+=1
            low+=1
        elif num[mid]==1:
            mid+=1
        else:
            num[mid],num[high]=num[high],num[mid]
            high-=1

            