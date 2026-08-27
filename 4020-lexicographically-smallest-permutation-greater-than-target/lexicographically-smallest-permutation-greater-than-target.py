class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
            
        for i in range(n - 1, -1, -1):
            cur_counts = list(counts)
            valid_prefix = True
            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if cur_counts[idx] > 0:
                    cur_counts[idx] -= 1
                else:
                    valid_prefix = False
                    break
            
            if not valid_prefix:
                continue
                
            for c in range(ord(target[i]) - ord('a') + 1, 26):
                if cur_counts[c] > 0:
                    cur_counts[c] -= 1
                    res = list(target[:i]) + [chr(ord('a') + c)]
                    for rem_c in range(26):
                        res.append(chr(ord('a') + rem_c) * cur_counts[rem_c])
                    return "".join(res)
                    
        return ""