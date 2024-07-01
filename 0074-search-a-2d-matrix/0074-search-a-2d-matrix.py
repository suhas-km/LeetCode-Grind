class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        for i in range(n):
            if target==matrix[i][0]:
                return True
            if target<matrix[i][0]:
                break
        if target in matrix[i-1]:
            return True
        if target in matrix[n-1]:
            return True
        return False