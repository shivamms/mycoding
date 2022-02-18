class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        i, n = 0, len(words)
        while i < n:
            words[i] = ''.join(list(words[i])[::-1])
            i += 1
        return ' '.join(words)
            
            