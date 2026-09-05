class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        curr_max = float('-inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            if curr_max - suffix_min[i] <= k:
                return i
                
        return -1