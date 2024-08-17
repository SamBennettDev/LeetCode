class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = left + ((right - left) // 2)
            square = mid * mid

            if square > x:
                right = mid - 1

            elif square < x:
                left = mid + 1
            
            elif square == x:
                return mid

        return right
        