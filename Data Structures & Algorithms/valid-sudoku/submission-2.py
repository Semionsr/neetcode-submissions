class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker_row = defaultdict(set)
        checker_col = defaultdict(set)
        checker_sqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in checker_row[r] 
                    or board[r][c] in checker_col[c] 
                    or board[r][c] in checker_sqr[(r // 3, c // 3)]):
                    return False
                
                    
                
                checker_row[r].add(board[r][c])
                checker_col[c].add(board[r][c])
                checker_sqr[(r // 3, c // 3)].add(board[r][c])

        return True

