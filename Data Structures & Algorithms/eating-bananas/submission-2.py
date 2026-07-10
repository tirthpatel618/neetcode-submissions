class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # total time needed decreases as eating speed increases
        # sorted search space is 1 to max(piles) -> bs on eating time
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k + 1
        return res
        