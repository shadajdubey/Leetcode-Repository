class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        num_set = set(nums)
        mult = k
        while mult in num_set:
            mult += k
        return mult