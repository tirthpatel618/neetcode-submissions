class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue to store indices of elements in decreasing order of values
        # smaller elements are removed when pushing a new number
        # if the element at the front of the queue falls out of the window, remove it

        res = []
        q = deque() # holds index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                #remove indices whos values are smaller than the new value as they cannpt be future max
                q.pop()
            q.append(r)

            if l > q[0]: # if the left pointer of the window is outside the top index, remove it
            # ie the old max is no longer inside the window
                q.popleft()

            if (r + 1) >= k:
                # when the window reaches size k, the front of the queue is the max
                res.append(nums[q[0]])
                #only increment the left pointer when window is at max size
                l += 1
            r += 1
        return res

        