class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        for i, c in enumerate(seq):
            if c == '(':
                res.append(i & 1)
            else:
                res.append(1 - (i & 1))
        return res