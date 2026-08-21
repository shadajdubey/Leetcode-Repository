class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return count