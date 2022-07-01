class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append([c,1])
            else:
                last_char, count = stack[-1]
                if c == last_char:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([c,1])
        return ''.join(c * count for c, count in stack)
            
                