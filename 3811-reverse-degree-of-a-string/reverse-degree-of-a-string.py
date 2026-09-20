class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            rev_alphabet_pos = ord('z') - ord(ch) + 1
            total += rev_alphabet_pos * i
        return total