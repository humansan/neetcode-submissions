class Solution:
    def isValid(self, s: str) -> bool:
        
        closing = {
            '(':')',
            "{":"}",
            "[":"]"
        }

        stack = []

        for char in s:
            if char in closing:
                stack.append(char)
            else:
                if stack and char == closing[stack[-1]]:
                    stack.pop()
                else:
                    return False                
        
        if stack:
            return False

        return True