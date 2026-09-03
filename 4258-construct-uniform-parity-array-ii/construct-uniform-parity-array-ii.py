class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        for x in nums1:
            if x % 2 != 0:
                return False
                
        return True