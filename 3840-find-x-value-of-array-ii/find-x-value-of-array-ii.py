from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]

        def pull(node: int, left: int, right: int):
            tree_prod[node] = (tree_prod[left] * tree_prod[right]) % k
            for r in range(k):
                tree_cnt[node][r] = tree_cnt[left][r]
            p_left = tree_prod[left]
            for r in range(k):
                tree_cnt[node][(p_left * r) % k] += tree_cnt[right][r]

        def build(node: int, l: int, r: int):
            if l == r:
                rem = nums[l] % k
                tree_prod[node] = rem
                tree_cnt[node][rem] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node, 2 * node, 2 * node + 1)

        def update(node: int, l: int, r: int, idx: int, val: int):
            if l == r:
                tree_cnt[node] = [0] * k
                rem = val % k
                tree_prod[node] = rem
                tree_cnt[node][rem] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, r, idx, val)
            pull(node, 2 * node, 2 * node + 1)

        def query_tree(node: int, l: int, r: int, ql: int, qr: int):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node][:]
            mid = (l + r) // 2
            if qr <= mid:
                return query_tree(2 * node, l, mid, ql, qr)
            if ql > mid:
                return query_tree(2 * node + 1, mid + 1, r, ql, qr)
            p1, c1 = query_tree(2 * node, l, mid, ql, qr)
            p2, c2 = query_tree(2 * node + 1, mid + 1, r, ql, qr)
            res_p = (p1 * p2) % k
            res_c = list(c1)
            for rem in range(k):
                res_c[(p1 * rem) % k] += c2[rem]
            return res_p, res_c

        build(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            nums[idx] = val
            update(1, 0, n - 1, idx, val)
            _, counts = query_tree(1, 0, n - 1, start, n - 1)
            ans.append(counts[x])

        return ans