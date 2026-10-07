class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        n=len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[j][i],mat[i][j]=mat[i][j],mat[j][i]

        for i in range(n):
            mat[i].reverse()        



        