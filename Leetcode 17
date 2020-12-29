class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if not digits:
            return []
        if len(digits) == 1:
            return list(dic[digits])
        
        head = digits[0]
        rest = digits[1:]
        rest_combo = self.letterCombinations(rest)

        return [i+j for j in rest_combo for i in dic[head]]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        
        def DFS(indx, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for c in d[digits[indx]]:
                DFS(indx+1, path+c)
                
        DFS(0, '')
        return res
