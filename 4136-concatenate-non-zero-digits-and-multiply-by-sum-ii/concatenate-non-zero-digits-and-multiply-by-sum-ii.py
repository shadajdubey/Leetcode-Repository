class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        nz_indices = [i for i, ch in enumerate(s) if ch != '0']
        k = len(nz_indices)
        
        if k == 0:
            return [0] * len(queries)
            
        pos_in_nz = [-1] * m
        for idx, orig_i in enumerate(nz_indices):
            pos_in_nz[orig_i] = idx
            
        next_nz = [-1] * m
        curr = -1
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                curr = i
            next_nz[i] = curr
            
        prev_nz = [-1] * m
        curr = -1
        for i in range(m):
            if s[i] != '0':
                curr = i
            prev_nz[i] = curr
            
        pref_sum = [0] * (k + 1)
        pref_val = [0] * (k + 1)
        
        for i, idx in enumerate(nz_indices):
            val = int(s[idx])
            pref_sum[i + 1] = pref_sum[i] + val
            pref_val[i + 1] = (pref_val[i] * 10 + val) % MOD
            
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            first_idx = next_nz[l]
            last_idx = prev_nz[r]
            
            if first_idx == -1 or last_idx == -1 or first_idx > r or last_idx < l:
                ans.append(0)
                continue
                
            q_l = pos_in_nz[first_idx]
            q_r = pos_in_nz[last_idx]
            
            digit_sum = pref_sum[q_r + 1] - pref_sum[q_l]
            #Shadaj Dubey
            length = q_r - q_l + 1
            x = (pref_val[q_r + 1] - pref_val[q_l] * pow10[length]) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans