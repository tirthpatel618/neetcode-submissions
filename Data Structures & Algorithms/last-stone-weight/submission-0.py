class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        print(stones)
        heapq.heapify(stones)
        # two heaviest stones are [0] and then the second one

        while True:
            if len(stones) == 0:
                return 0
            elif len(stones) == 1:
                return abs(stones[0])
            
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)
            


        