import math


class SparseTable:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        if self.n == 0:
            return
        self.k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.k)]
        self.st[0] = list(nums)

        for i in range(1, self.k):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l: int, r: int) -> int:
        if l > r or self.n == 0 or l < 0 or r >= self.n:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:

    def maxActiveSectionsAfterTrade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        n = len(s)
        zero_groups = []
        zero_group_index = []

        for i, char in enumerate(s):
            if char == "0":
                if i > 0 and s[i - 1] == "0":
                    zero_groups[-1]["len"] += 1
                else:
                    zero_groups.append({"start": i, "len": 1})
            zero_group_index.append(len(zero_groups) - 1)

        zero_merge_lens = [
            zero_groups[i]["len"] + zero_groups[i + 1]["len"]
            for i in range(len(zero_groups) - 1)
        ]

        st = SparseTable(zero_merge_lens)
        ones_count = s.count("1")

        ans = []
        for l, r in queries:
            g_l = zero_group_index[l]
            g_r = zero_group_index[r]

            left_len = (
                0
                if g_l == -1
                else zero_groups[g_l]["len"] - (l - zero_groups[g_l]["start"])
            )
            right_len = 0 if g_r == -1 else (r - zero_groups[g_r]["start"] + 1)

            g_r_adj = g_r if s[r] == "1" else g_r - 1
            start_adj = g_l + 1
            end_adj = g_r_adj - 1

            active_sections = ones_count

            if s[l] == "0" and s[r] == "0" and g_l + 1 == g_r:
                active_sections = max(
                    active_sections, ones_count + left_len + right_len
                )

            if start_adj <= end_adj:
                active_sections = max(
                    active_sections, ones_count + st.query(start_adj, end_adj)
                )

            if s[l] == "0" and g_l + 1 <= g_r_adj:
                active_sections = max(
                    active_sections,
                    ones_count + left_len + zero_groups[g_l + 1]["len"],
                )

            if s[r] == "0" and g_l < g_r - 1:
                active_sections = max(
                    active_sections,
                    ones_count + right_len + zero_groups[g_r - 1]["len"],
                )

            ans.append(active_sections)

        return ans