class Solution:
    def spiralOrder(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n=len(mat[0])
        right,bottom,left,top=n-1,m-1,0,0
        ans=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(mat[top][i])
            top+=1
            
            for i in range(top,bottom+1):
                ans.append(mat[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(mat[bottom][i])  
                bottom-=1
            if left<=right:  
                for i in range(bottom,top-1,-1):
                    ans.append(mat[i][left])    
                left+=1  
        return ans             



       