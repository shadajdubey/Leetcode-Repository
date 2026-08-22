class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        temp = n
        
        while temp > 0:
            d = temp % 10
            digit_sum += d
            digit_prod *= d
            temp //= 10
            
        return n % (digit_sum + digit_prod) == 0