class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col = len(matrix), len(matrix[0])
        
        top, bot = 0, row - 1
        while top <= bot:
            line = (top + bot) // 2
            if target > matrix[line][-1]:
                top = line + 1
            elif target < matrix[line][0]:
                bot = line - 1
            else:
                break

        if not (top <= bot):
            return False
        
        line = (top + bot) // 2
        l , r = 0 , col-1
        while l <= r:
            middle = (l+r)//2
            if target > matrix[line][middle]:
                l = middle+1
            elif target < matrix[line][middle]:
                r = middle-1
            else:
                return True
        return False
