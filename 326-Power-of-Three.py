class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def recur(n):
            if n <= 0:
                return False
            elif n == 1:
                return True
            elif n%3 != 0:
                return False
            return recur(float(n/3))
        
        return recur(n)
        