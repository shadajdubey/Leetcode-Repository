class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q_diff = 0
        
        for i in range(n // 2):
            if num[i] == '?':
                q_diff += 1
            else:
                diff += int(num[i])
                
        for i in range(n // 2, n):
            if num[i] == '?':
                q_diff -= 1
            else:
                diff -= int(num[i])
                
        return diff * 2 != -q_diff * 9