class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')' and '(' != stack[-1]:
                    return False
                if char == '}' and '{' != stack[-1]:
                    return False
                if char == ']' and '[' != stack[-1]:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True
