from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        ans = 0
        for i, count in enumerate(sorted_freqs):
            ans += count * (i // 8 + 1)
            
        return ans