class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        res = set()


        def backtrack(i,r,c):
            if i == len(word):
                return True
            if (r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or len(res) > len(word) or 
                board[r][c] != word[i] or (r,c) in res):
                return False
            
            res.add((r,c))
            total =  (backtrack(i+1, r+1,c) or
                    backtrack(i+1, r,c+1) or
                    backtrack(i+1, r-1,c) or 
                    backtrack(i+1, r,c-1))
            res.remove((r,c))
            return total
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0,r,c):
                    return True
        return False
        
    
            


            