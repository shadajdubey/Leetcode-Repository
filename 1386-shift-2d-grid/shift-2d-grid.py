class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        flat = flat[-k:] + flat[:-k]
        
        result = []
        for i in range(0, total, n):
            result.append(flat[i:i+n])
            
        return result