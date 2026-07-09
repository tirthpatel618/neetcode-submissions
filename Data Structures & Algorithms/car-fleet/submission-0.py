class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #while loop. positions are updated every 
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # closest to target first
        stack = []
        for p, s in pair:
            # first compute time it takes to get to target
            time = (target - p) / s
            stack.append(time)
            #if the new cars time is less than or equal to the time before it, it is merged with that fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

