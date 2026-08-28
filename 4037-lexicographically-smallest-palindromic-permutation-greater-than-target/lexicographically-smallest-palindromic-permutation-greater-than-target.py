class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        total_count = Counter(s)

        odd_chars = [c for c, count in total_count.items() if count % 2 != 0]
        if (n % 2 == 0 and len(odd_chars) > 0) or (n % 2 == 1 and len(odd_chars) != 1):
            return ""

        mid_char = odd_chars[0] if n % 2 == 1 else ""
        half_count = {c: total_count[c] // 2 for c in total_count if total_count[c] // 2 > 0}
        m = n // 2

        def build_palindrome(first_half: str) -> str:
            return first_half + mid_char + first_half[::-1]

        target_half_count = Counter(target[:m])
        if target_half_count == Counter({c: cnt for c, cnt in half_count.items() if cnt > 0}):
            cand = build_palindrome(target[:m])
            if cand > target:
                return cand

        prefix_count = Counter()
        for i in range(m):
            prefix_count[target[i]] += 1

        for i in range(m - 1, -1, -1):
            prefix_count[target[i]] -= 1
            if prefix_count[target[i]] == 0:
                del prefix_count[target[i]]

            if any(prefix_count[c] > half_count.get(c, 0) for c in prefix_count):
                continue

            rem_counts = {c: half_count[c] - prefix_count.get(c, 0) for c in half_count}

            for code in range(ord(target[i]) + 1, ord("z") + 1):
                c = chr(code)
                if rem_counts.get(c, 0) > 0:
                    rem_counts[c] -= 1
                    rest = []
                    for ch in sorted(rem_counts.keys()):
                        rest.append(ch * rem_counts[ch])
                    first_half = target[:i] + c + "".join(rest)
                    return build_palindrome(first_half)

        return ""