class Solution:
    def sortColors(self, num: list[int]) -> None:
        
        n = len(num)
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(n):

            if num[i] == 0:
                count0 += 1
            elif num[i] == 1:
                count1 += 1
            else:
                count2 += 1
        for i in range(count0):
            num[i]=0
        for i in range(count0,count0+count1):
            num[i]=1
        for i in range(count0+count1,n):    
            num[i]=2

