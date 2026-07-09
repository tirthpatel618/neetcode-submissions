class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # maxheap for left side of median
        self.minHeap = [] # minheap for right side of median
        

    def addNum(self, num: int) -> None:
        #push into the top half if 
        # its greater than the smallest number in the top
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        #rebalance it 
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return ((-self.maxHeap[0]) + self.minHeap[0]) / 2
        
        