class Solution:
    def setZeroes(self, mat: list[list[int]]) -> None:
        r=len(mat)
        c=len(mat[0])
        rt=[0 for _ in range(r)]
        ct=[0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    rt[i]=-1
                    ct[j]=-1
                    
        for i in range(r):
            for j in range(c):
                if rt[i]==-1 or ct[j]==-1:
                    mat[i][j]=0
        