class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            
            new_subsequences = (sum(ends_with) + 1) % MOD
            ends_with[idx] = new_subsequences
            
        return sum(ends_with) % MOD