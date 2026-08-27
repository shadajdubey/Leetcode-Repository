class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        
        for i in range(n):
            count = 0
            for j in range(i, n):
                if s[j] == '1':
                    count += 1
                if count == k:
                    sub = s[i:j+1]
                    if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                        ans = sub
                    break
                    
        return ans