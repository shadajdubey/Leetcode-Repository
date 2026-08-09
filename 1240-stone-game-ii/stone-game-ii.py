class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            if (i, M) in memo:
                return memo[(i, M)]

            min_opponent = float('inf')
            for X in range(1, 2 * M + 1):
                min_opponent = min(min_opponent, dp(i + X, max(M, X)))

            memo[(i, M)] = suffix_sum[i] - min_opponent
            return memo[(i, M)]

        return dp(0, 1)