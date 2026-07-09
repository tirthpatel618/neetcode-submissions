class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a min heap of size k 
        heap = []
        # delete a number as as soon as heapsize is greater than k. 
        # therefore n * log k 
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]

        