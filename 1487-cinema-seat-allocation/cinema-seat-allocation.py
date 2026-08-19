from collections import defaultdict
from typing import List


class Solution:

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    # Map row -> bitmask of reserved seats (focusing on seats 2 to 9)
    # Using 1-indexed bit positions for clarity
    row_mask = defaultdict(int)

    for r, c in reservedSeats:
      if 2 <= c <= 9:
        row_mask[r] |= 1 << c

    # Left:  seats 2, 3, 4, 5 -> bits: (1<<2 | 1<<3 | 1<<4 | 1<<5)
    LEFT_MASK = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
    # Right: seats 6, 7, 8, 9 -> bits: (1<<6 | 1<<7 | 1<<8 | 1<<9)
    RIGHT_MASK = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
    # Mid:   seats 4, 5, 6, 7 -> bits: (1<<4 | 1<<5 | 1<<6 | 1<<7)
    MID_MASK = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)

    allocated_groups = 0

    for r, mask in row_mask.items():
      can_left = (mask & LEFT_MASK) == 0
      can_right = (mask & RIGHT_MASK) == 0
      can_mid = (mask & MID_MASK) == 0

      if can_left and can_right:
        allocated_groups += 2
      elif can_left or can_right or can_mid:
        allocated_groups += 1

    # Completely unreserved rows can fit 2 groups each
    empty_rows = n - len(row_mask)
    allocated_groups += empty_rows * 2

    return allocated_groups