class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on h
        # upper bound for it is max(piles), since h is atleast the len of piles. 
        # lower bound is 1. search through it to find the optimal rate

        #key point - total time needed decreases as eating speed increases 

        left = 1
        right = max(piles)

        res = right

        while left <= right:
            k = (left + right) // 2 # set k to be the mid to test
            
            #calculate time needed at that speed
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                right = k-1 # lower mid
            else:
                left = k + 1 # upper mid
        return res
