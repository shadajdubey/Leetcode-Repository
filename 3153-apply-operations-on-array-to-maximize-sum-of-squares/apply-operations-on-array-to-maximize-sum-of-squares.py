class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        # Count the frequency of each set bit
        for num in nums:
            for bit in range(30):
                if (num >> bit) & 1:
                    bit_counts[bit] += 1
        
        # Construct the top k numbers greedily
        top_k = [0] * k
        for bit in range(30):
            count = bit_counts[bit]
            for i in range(min(count, k)):
                top_k[i] |= (1 << bit)
                
        # Calculate the sum of squares modulo 10^9 + 7
        ans = 0
        for num in top_k:
            ans = (ans + num * num) % MOD
            
        return ans