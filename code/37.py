# Approach 1:
# This approach is very slow, because for each step, we need to check is its validity (3 * n).

class Solution:

		def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(x,y,value):
            if any(
                board[x][i] == value or
                board[i][y] == value or
                board[(x//3)*3+i//3][(y//3)*3+i%3] == value
                for i in range(9)
            ):
                return False

            return True


        def sudokuSolve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1,10):
                            if valid(i,j,str(k)):
                                board[i][j] = str(k)
                                if sudokuSolve():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        sudokuSolve()

# Approach 2:

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col, box, need = defaultdict(set), defaultdict(set), defaultdict(set), []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i // 3, j // 3)].add(board[i][j])
                else:
                    need.append((i , j))

        def dfs(need):
            if not need:
                return True
            r, c = need[-1]
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if num not in row[r] and num not in col[c] and num not in box[(r // 3, c // 3)]:
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    box[(r // 3, c // 3)].add(num)
                    need.pop()
                    if dfs(need):
                        return True
                    board[r][c] = "."
                    row[r].remove(num)
                    col[c].remove(num)
                    box[(r // 3, c // 3)].remove(num)
                    need.append((r, c))
            return False
