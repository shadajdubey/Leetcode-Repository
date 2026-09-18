class Solution:

  def maxNumOfSubstrings(self, s: str) -> list[str]:
    
    first = {}
    last = {}
    for i, ch in enumerate(s):
      if ch not in first:
        first[ch] = i
      last[ch] = i

  
    def get_valid_right(i: int) -> int:
      right = last[s[i]]
      j = i
      while j <= right:
        c = s[j]
        
        if first[c] < i:
          return -1
        right = max(right, last[c])
        j += 1
      return right

    
    intervals = []
    for c in first:
      start = first[c]
      end = get_valid_right(start)
      if end != -1:
        intervals.append((start, end))

    
    intervals.sort(key=lambda x: x[1])

    res = []
    prev_end = -1
    for start, end in intervals:
      if start > prev_end:
        res.append(s[start : end + 1])
        prev_end = end

    return res