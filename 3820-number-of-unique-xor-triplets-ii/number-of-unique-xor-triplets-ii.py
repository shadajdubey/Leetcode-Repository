class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        current_xors = {0}
        
        for _ in range(3):
            next_xors = set()
            for x in current_xors:
                for num in unique_nums:
                    next_xors.add(x ^ num)
            current_xors = next_xors
            
        return len(current_xors)