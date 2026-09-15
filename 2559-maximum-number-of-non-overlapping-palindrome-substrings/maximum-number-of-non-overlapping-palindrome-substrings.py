class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1

        for center in range(2 * n - 1):
            l = center // 2
            r = l + (center % 2)

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    if l > last_end:
                        ans += 1
                        last_end = r
                        break
                    else:
                        break
                l -= 1
                r += 1

        return ans