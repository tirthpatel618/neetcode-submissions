"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        First sort the array by start time. 
        Conflict if start[i] > end[i-1]
        but then how do you track when that conflict is resolved?
        Min heap? at every start time check if the earliest conflict to end is ended or not
        """

        intervals.sort(key=lambda x: x.start)
        minHeap = [] # minHeap tracks current conflicts and when they will end
        rooms = 0
        for i in range(len(intervals)):
            time = intervals[i].start
            while minHeap and time >= minHeap[0]:
                heapq.heappop(minHeap) # get rid of all finished meetings
            
            heapq.heappush(minHeap, intervals[i].end) # always just push it onto the heap
            rooms = max(rooms, len(minHeap)) # Heap is meetings going on concurrently. 

        return rooms






        