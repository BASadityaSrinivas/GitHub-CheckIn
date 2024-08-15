class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        arr = [-1] * (n+1)
        arr[0] = 0
        arr[1] = 1

        def recur(arr, n):
            if arr[n] != -1:
                return arr[n]   
            else:
                calc = recur(arr, n-1) + recur(arr, n-2)
                arr[n] = calc
            return calc
        
        recur(arr, n)
        return arr[n]
