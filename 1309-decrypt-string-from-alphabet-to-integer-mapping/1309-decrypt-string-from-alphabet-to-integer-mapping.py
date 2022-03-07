class Solution:
    def freqAlphabets(self, s: str) -> str:
        ## using xtra space - 98%
        # n = len(s)
        # queue = [s[0]]
        # for i in range(1,n):
        #     if s[i] == '#':
        #         l2, l1 = queue.pop(), queue.pop()
        #         queue.append(l1+l2)
        #     else:
        #         queue.append(s[i])
        # return ''.join([chr(96+int(x)) for x in queue])
    
        ## without xtra space
        decrypted, i = '', len(s)-1
        while i >= 0:
            if s[i] == '#':
                decrypted += chr(96+int(s[i-2:i]))
                i -= 3
            else:
                decrypted += chr(96+int(s[i]))
                i -= 1
        return decrypted[::-1]
        