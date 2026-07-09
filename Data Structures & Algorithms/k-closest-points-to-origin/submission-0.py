class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x, y):
            return x**2 + y**2

        heap = []

        for x, y in points:
            dist = distance(x, y)
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [[x, y] for neg_dist, x, y in heap]


        
        