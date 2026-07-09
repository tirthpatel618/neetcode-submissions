class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        always schedule the task that has the highest freq first (if avail)
        track availability through queue
        Once it is avail - move it back onto the heap
        """
        time = 0
        # hashmap - task : occurence
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # pairs of [cnt, idletime]
        # stores - [remaining count after running, next avail time]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                #do the task with the highest occurence left
                remaining = 1 + heapq.heappop(maxHeap) # negative vals
                if remaining: #add to the queue if there are any remaining
                    q.append([remaining, time + n]) 
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
