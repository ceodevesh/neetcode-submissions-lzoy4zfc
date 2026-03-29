class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        lo,hi=1,max(piles)
        while lo<hi:
            mid = (lo+hi)//2
            res = 0
            for p in piles:
                res+= math.ceil(p/mid)
            if res <=h:
                hi = mid
            else:
                lo = mid + 1
        return lo
