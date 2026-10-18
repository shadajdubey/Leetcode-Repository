class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to compute digit sum
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        # Pair each number with its (digit_sum, value, original_index)
        arr = []
        for i, x in enumerate(nums):
            arr.append((digit_sum(x), x, i))
            
        # Sort based on digit sum, then by value (as a tie-breaker)
        arr.sort(key=lambda item: (item[0], item[1]))
        
        # Find the minimum swaps using cycle sort / graph cycles
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, continue
            if visited[i] or arr[i][2] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
                
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps