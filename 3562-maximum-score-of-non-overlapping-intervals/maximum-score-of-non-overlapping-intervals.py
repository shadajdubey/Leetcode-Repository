from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
       
        events = sorted([(r, l, w, i) for i, (l, r, w) in enumerate(intervals)])
        r_vals = [e[0] for e in events]
        
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            r, l, w, idx = events[i - 1]
            
            
            prev = bisect_left(r_vals, l)
            
            for k in range(1, 5):
                
                best_score, best_ids = dp[i - 1][k]
                
                
                prev_score, prev_ids = dp[prev][k - 1]
                cand_score = prev_score + w
                cand_ids = tuple(sorted(prev_ids + (idx,)))
                
                
                if cand_score > best_score:
                    best_score, best_ids = cand_score, cand_ids
                elif cand_score == best_score and cand_ids < best_ids:
                    best_ids = cand_ids
                
                dp[i][k] = (best_score, best_ids)
        
       
        max_score = 0
        ans = ()
        for k in range(1, 5):
            score, ids = dp[n][k]
            if score > max_score:
                max_score = score
                ans = ids
            elif score == max_score and ids < ans:
                ans = ids
                
        return list(ans)