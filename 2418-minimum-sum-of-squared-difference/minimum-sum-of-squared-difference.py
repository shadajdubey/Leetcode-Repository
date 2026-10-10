class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        if sum(diffs) <= total_k:
            return 0
        
        max_val = max(diffs)
        count = [0] * (max_val + 1)
        for d in diffs:
            count[d] += 1
            
        rem = total_k
        for i in range(max_val, 0, -1):
            if count[i] > 0:
                take = min(count[i], rem)
                count[i] -= take
                count[i - 1] += take
                rem -= take
                if rem == 0:
                    break
                    
        return sum(i * i * count[i] for i in range(max_val + 1))