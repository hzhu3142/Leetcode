class Solution:
    def __init__(self):
        self.res = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for j in range(n)]
        self.backtracking(board, 0)
        return self.res
    
    def backtracking(self, board, row):
        if row == len(board):
            temp = copy.deepcopy(board)
            self.res.append(["".join(row) for row in temp])
            return
        
        n = len(board[row])
        for col in range(n):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.backtracking(board, row+1)
                board[row][col] = '.'                     
            
    def isValid(self, board, row, col):
        n = len(board)
        for i in range(row+1):
            if board[i][col] == 'Q':
                return False

            if row >= i and col >= i and board[row-i][col-i] == 'Q':
                return False
        
            if 0 <= row+col-i < n and board[i][row+col-i] == 'Q':
                return False
        
        return True
        
