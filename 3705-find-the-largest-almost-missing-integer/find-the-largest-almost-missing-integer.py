from collections import defaultdict
from typing import List


class Solution:

  def largestInteger(self, nums: List[int], k: int) -> int:
    n = len(nums)
    freq = defaultdict(int)

    for i in range(n - k + 1):
      seen = set(nums[i : i + k])
      for x in seen:
        freq[x] += 1

    ans = -1
    for x, count in freq.items():
      if count == 1:
        ans = max(ans, x)

    return ans