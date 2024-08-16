class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recur(n):
            if n <= 0:
                return False
            elif n == 1:
                return True
            return recur(float(n/4))
        
        return recur(n)