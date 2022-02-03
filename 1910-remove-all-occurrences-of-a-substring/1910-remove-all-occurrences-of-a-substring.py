class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:        
        part = list(part)
        ws = len(part)
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-ws::] == part:
                stack = stack[:-ws]
        return "".join(stack)
        