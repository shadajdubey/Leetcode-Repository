class Solution:

  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    t = "1" + s + "1"
    blocks = []
    for char in t:
      if not blocks or blocks[-1][0] != char:
        blocks.append([char, 1])
      else:
        blocks[-1][1] += 1

    ans = s.count("1")
    max_delta = 0

    for i in range(1, len(blocks) - 1):
      if (
          blocks[i][0] == "1"
          and blocks[i - 1][0] == "0"
          and blocks[i + 1][0] == "0"
      ):
        max_delta = max(max_delta, blocks[i - 1][1] + blocks[i + 1][1])

    return ans + max_delta