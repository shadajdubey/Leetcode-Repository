from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litter_map = {}
        
        # Find start position and index all litter locations
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start = (r, c)
                elif cell == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        total_litter = len(litter_map)
        if total_litter == 0:
            return 0
            
        target_mask = (1 << total_litter) - 1
        
        # max_energy[r][c][mask] stores the maximum energy seen for this state
        max_energy = [[[-1] * (1 << total_litter) for _ in range(n)] for _ in range(m)]
        
        sr, sc = start
        queue = deque([(sr, sc, 0, energy, 0)]) # (r, c, mask, current_energy, steps)
        max_energy[sr][sc][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacle
                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                    continue
                
                # Moving costs 1 unit of energy
                next_energy = cur_energy - 1
                if next_energy < 0:
                    continue
                    
                next_mask = mask
                cell = classroom[nr][nc]
                
                if cell == 'R':
                    next_energy = energy
                elif cell == 'L' and (nr, nc) in litter_map:
                    next_mask |= (1 << litter_map[(nr, nc)])
                
                # Check if all litters are collected
                if next_mask == target_mask:
                    return steps + 1
                
                # Prune if we have already reached this state with higher or equal energy
                if next_energy > max_energy[nr][nc][next_mask]:
                    max_energy[nr][nc][next_mask] = next_energy
                    # Can only continue moving if energy > 0 or on a reset tile
                    if next_energy > 0 or cell == 'R':
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1