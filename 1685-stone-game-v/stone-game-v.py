from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            k = 0
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                
                if i == 0 or k < i:
                    k = i
                while k < j and (prefix[k + 1] - prefix[i]) * 2 < total:
                    k += 1
                
                res = 0
                if (prefix[k + 1] - prefix[i]) * 2 == total:
                    res = max(max_left[i][k], max_right[k + 1][j])
                else:
                    if k > i:
                        res = max(res, max_left[i][k - 1])
                    if k < j:
                        res = max(res, max_right[k + 1][j])
                        
                dp[i][j] = res
                max_left[i][j] = max(max_left[i][j - 1], total + res)
                max_right[i][j] = max(max_right[i + 1][j], total + res)
                
        return dp[0][n - 1]