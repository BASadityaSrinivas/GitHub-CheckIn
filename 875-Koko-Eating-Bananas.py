import math

class Solution:
    def calc_h(self, piles, k):
        h = 0
        for i in piles:
            h += math.ceil(i/k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
    
        while l <= r:
            mid = (l+r)//2
            hour = self.calc_h(piles, mid)

            if hour <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res