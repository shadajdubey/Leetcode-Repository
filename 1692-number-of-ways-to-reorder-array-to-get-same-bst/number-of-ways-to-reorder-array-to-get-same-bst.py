class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            return comb(len(left) + len(right), len(left)) * helper(left) * helper(right) % MOD
            
        return (helper(nums) - 1) % MOD