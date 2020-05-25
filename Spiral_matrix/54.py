class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        left,right = 0, col-1
        up,down = 0, row-1
        
        while left < right and up < down :
            for i in range(left,right):
                ans.append(matrix[up][i])
            for i in range(up,down):
                ans.append(matrix[i][right])
            for i in range(right,left,-1):
                ans.append(matrix[down][i])
            for i in range(down,up,-1):
                ans.append(matrix[i][left])
            left,right,up,down = left+1,right-1,up+1,down-1
            
        if left == right:
            for i in range(up,down+1):
                ans.append(matrix[i][left])
        elif up == down:
            for i in range(left,right+1):
                ans.append(matrix[up][i])
        return ans 
        
        
        