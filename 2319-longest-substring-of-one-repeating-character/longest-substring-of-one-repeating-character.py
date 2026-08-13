class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.lc = [''] * (4 * self.n)
        self.rc = [''] * (4 * self.n)
        self.pref = [0] * (4 * self.n)
        self.suff = [0] * (4 * self.n)
        self.mx = [0] * (4 * self.n)
        self.build(s, 1, 0, self.n - 1)

    def merge(self, node: int, l_len: int, r_len: int):
        left = 2 * node
        right = 2 * node + 1
        self.lc[node] = self.lc[left]
        self.rc[node] = self.rc[right]
        
        self.pref[node] = self.pref[left]
        if self.pref[left] == l_len and self.rc[left] == self.lc[right]:
            self.pref[node] += self.pref[right]
            
        self.suff[node] = self.suff[right]
        if self.suff[right] == r_len and self.rc[left] == self.lc[right]:
            self.suff[node] += self.suff[left]
            
        self.mx[node] = max(self.mx[left], self.mx[right])
        if self.rc[left] == self.lc[right]:
            self.mx[node] = max(self.mx[node], self.suff[left] + self.pref[right])

    def build(self, s: str, node: int, l: int, r: int):
        if l == r:
            self.lc[node] = self.rc[node] = s[l]
            self.pref[node] = self.suff[node] = self.mx[node] = 1
            return
        mid = (l + r) // 2
        self.build(s, 2 * node, l, mid)
        self.build(s, 2 * node + 1, mid + 1, r)
        self.merge(node, mid - l + 1, r - mid)

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.lc[node] = self.rc[node] = ch
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, ch)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, ch)
        self.merge(node, mid - l + 1, r - mid)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        for i in range(len(queryIndices)):
            st.update(1, 0, len(s) - 1, queryIndices[i], queryCharacters[i])
            ans.append(st.mx[1])
        return ans