class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [(i+1) for i in range(n)]
        count = 1
        cur = 0
        
        while len(arr) > 1:
            if count == k:
                arr.pop(cur)
                count = 1
                if cur > len(arr)-1:
                    cur = 0
            else:
                count += 1
                if cur == len(arr)-1:
                    cur = 0
                else:
                    cur += 1
        
        return arr[0]
