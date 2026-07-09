class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            comp[i] = curr_id
            
        return [comp[u] == comp[v] for u, v in queries]