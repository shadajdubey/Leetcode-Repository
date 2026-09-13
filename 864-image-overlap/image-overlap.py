from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        counts = defaultdict(int)
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                counts[(r1 - r2, c1 - c2)] += 1
                
        return max(counts.values(), default=0)