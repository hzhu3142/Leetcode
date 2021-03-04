class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        matched = []
        def backtrack(row, col, curTrie):
            letter = board[row][col]
            curr = curTrie[letter]
            if '#' in curr:
                matched.append(curr.pop('#'))
            board[row][col] = '#'
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = row+a, col+b
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] not in curr:
                    continue
                backtrack(x, y, curr)
            board[row][col] = letter
            if not curr:
                curTrie.pop(letter) # to cut off the path, which has no '#' at end.
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root:
                    backtrack(i, j, trie.root)
                    
        return matched
