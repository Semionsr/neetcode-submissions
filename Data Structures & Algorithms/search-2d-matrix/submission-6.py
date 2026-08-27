class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        #l, r = 0, len(matrix)-1

        while top <= bottom:
            middle = (top+bottom)//2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break

        if not (top <= bottom):
            return False
        middle = (top+bottom)//2

        l, r = 0, len(matrix[middle])-1

        while l <= r:
            m = (l+r)//2
            if target == matrix[middle][m]:
                return True
            if target > matrix[middle][m]:
                l = m + 1
            elif target < matrix[middle][m]:
                r = m - 1
        return False






