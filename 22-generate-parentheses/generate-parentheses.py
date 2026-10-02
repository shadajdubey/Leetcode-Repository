class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count: int, close_count: int, path: str):
            if open_count == n and close_count == n:
                res.append(path)
                return
                
            if open_count < n:
                backtrack(open_count + 1, close_count, path + "(")
                
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + ")")
                
        backtrack(0, 0, "")
        return res