class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker_col = defaultdict(set)
        checker_row = defaultdict(set)
        checker_sqr = defaultdict(set)
        

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in checker_col[col]:
                    return False
                elif board[row][col] in checker_row[row]:
                    return False
                elif board[row][col] in checker_sqr[(row // 3) , (col // 3)]:
                    return False


                checker_col[col].add(board[row][col])
                checker_row[row].add(board[row][col])
                checker_sqr[(row // 3) , (col // 3)].add(board[row][col])
        
        return True
                


                


