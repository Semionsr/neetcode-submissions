class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            middle = (top+bottom)//2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                break
        
        if not top <= bottom:
            return False
        
        middle = (top+bottom)//2

        l, r = 0, len(matrix[0])-1

        while l <= r:
            m = (r+l)//2
            if matrix[middle][m] == target:
                return True
            if matrix[middle][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
            
