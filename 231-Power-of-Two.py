class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # # Iterative
        
        # while n > 0:
        #     if n==float(1):
        #         return True
        #     n = float(n/2)
        
        # return False

        # # Recursive
        
        def recur(n):
            if n == 1:
                return True
            if n <= 0:
                return False
            return recur(float(n/2))

        return recur(n)
        