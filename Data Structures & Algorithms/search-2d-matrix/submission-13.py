class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        # O(log(m * n))
        # 2d binary search
        # The first integer of every row is greater than the last integer of the previous row.


        L, R = 0, len(matrix) -1

        while L<=R:
            M = (L+R)//2
            if matrix[M][0] <= target <= matrix[M][-1]:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    m = (l+r)//2
                    if matrix[M][m] == target:
                        return True
                    if matrix[M][m] > target:
                        r = m-1
                    
                    if matrix[M][m] < target:
                        l = m + 1
                return False

            if matrix[M][0] > target:
                R = M -1
            if matrix[M][-1] < target:
                L = M + 1

                
                    
        
        return False

            

