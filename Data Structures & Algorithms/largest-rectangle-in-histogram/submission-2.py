class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # store a pair: (index, height)

        for i, h in enumerate(heights):
            start = i

            #while top height is greather than h, pop then new max and then 
            # the new bar can start from there
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            #push that new start onto stack
            stack.append((start, h))
        
        # need to compute area of bars that never encounter a smaller bar to the right
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
