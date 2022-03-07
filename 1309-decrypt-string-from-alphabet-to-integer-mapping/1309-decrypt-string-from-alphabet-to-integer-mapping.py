class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        queue = [s[0]]
        for i in range(1,n):
            if s[i] == '#':
                l2, l1 = queue.pop(), queue.pop()
                queue.append(l1+l2)
            else:
                queue.append(s[i])
        return ''.join([chr(96+int(x)) for x in queue])