class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #its greater then top of stack
                stackT, stackIdx = stack.pop() #pop the top
                res[stackIdx] = (i - stackIdx) # current day - day in stack that this temp is greater than
            stack.append([t, i])
        return res