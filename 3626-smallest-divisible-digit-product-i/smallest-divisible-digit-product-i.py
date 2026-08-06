class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num: int) -> int:
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod

        while digit_product(n) % t != 0:
            n += 1
        return n