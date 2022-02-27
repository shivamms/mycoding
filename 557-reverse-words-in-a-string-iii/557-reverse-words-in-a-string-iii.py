class Solution:
    def reverseWords(self, s: str) -> str:
        ## without using built-in list slicing
#         def reverse(word):
#             i, j = 0, len(word)-1
#             while i < j:
#                 word[i], word[j] = word[j], word[i]
#                 i += 1
#                 j -= 1
#             return ''.join(word)
        
#         words = s.split()
#         return ' '.join([reverse(list(word)) for word in words])
    
        ## using built-in list slicing  
        return ' '.join([word[::-1] for word in s.split(' ')])
        