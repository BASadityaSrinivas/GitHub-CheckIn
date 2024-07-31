class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            stack and stack.pop() if i == "*" else stack.append(i)
        
        return "".join(stack)
        