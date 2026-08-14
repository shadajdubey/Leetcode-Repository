from collections import Counter
from typing import List


class Solution:

  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    count = Counter()
    left = 0
    max_len = 0

    for right in range(len(nums)):
      count[nums[right]] += 1

      # Shrink the window if frequency exceeds k
      while count[nums[right]] > k:
        count[nums[left]] -= 1
        left += 1

      max_len = max(max_len, right - left + 1)

    return max_len