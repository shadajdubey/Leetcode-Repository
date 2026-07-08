import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)
        
        min_heap = []
        speed_sum = 0
        max_perf = 0
        
        for eff, sp in engineers:
            heapq.heappush(min_heap, sp)
            speed_sum += sp
            
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
                
            max_perf = max(max_perf, speed_sum * eff)
            
        return max_perf % (10**9 + 7)