import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        if sum(1 for v in count.values() if v % 2 == 1) > 1:
            return ""

        half_freq = [0] * 26
        mid = ""
        for c, freq in count.items():
            half_freq[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                mid = c

        if k > self._countArrangements(half_freq):
            return ""

        left = []
        half_len = sum(half_freq)

        for _ in range(half_len):
            for i in range(26):
                if half_freq[i] == 0:
                    continue
                half_freq[i] -= 1
                arrangements = self._countArrangements(half_freq)
                if arrangements >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    half_freq[i] += 1

        prefix_str = "".join(left)
        return prefix_str + mid + prefix_str[::-1]

    def _countArrangements(self, count: list[int]) -> int:
        total = sum(count)
        res = 1
        for freq in count:
            res *= self._nCk(total, freq)
            if res >= self.MAX:
                return self.MAX
            total -= freq
        return res

    def _nCk(self, n: int, k: int) -> int:
        res = 1
        for i in range(1, min(k, n - k) + 1):
            res = res * (n - i + 1) // i
            if res >= self.MAX:
                return self.MAX
        return res