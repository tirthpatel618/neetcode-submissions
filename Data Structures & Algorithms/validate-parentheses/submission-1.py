class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"]":"[", ")":"(", "}":"{"}
        for b in s:
            if b in brackets:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
        
        