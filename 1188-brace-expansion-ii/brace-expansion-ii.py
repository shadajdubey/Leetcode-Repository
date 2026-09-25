class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(exp: str, res: set):
            j = exp.find('}')
            if j == -1:
                res.add(exp)
                return
            i = exp.rfind('{', 0, j)
            
            before = exp[:i]
            middle = exp[i + 1:j]
            after = exp[j + 1:]
            
            for part in middle.split(','):
                dfs(before + part + after, res)

        result = set()
        dfs(expression, result)
        return sorted(list(result))