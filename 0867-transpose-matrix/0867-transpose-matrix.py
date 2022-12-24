class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(len(matrix[0])):
            transpose=[]
            for j in range(len(matrix)):
                transpose.append(matrix[j][i])
            result.append(transpose)
        return result
            