class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
#         def recurse(i, curr):
#             if i == len(alphaPos):
#                 return
#             pos = alphaPos[i]
#             lower = s[:pos]+s[pos].lower()+s[pos+1:]
#             upper = s[:pos]+s[pos].upper()+s[pos+1:]
#             output.add(lower)
#             output.add(upper)
#             recurse(i+1, lower)
#             recurse(i+1, upper)
            
#         n, output, alphaPos = len(s), set(), [] 
#         for i, char in enumerate(s):
#             if char.isalpha(): alphaPos.append(i)  
#         recurse(0,[])
#         return output
# #         n, output, alphaPos = len(s), set(), [] 
# #         for i, char in enumerate(s):
# #             if char.isalpha(): alphaPos.append(i) 
# #         queue, i, m = [s], 0, len(alphaPos)
# #         if m == 0:
# #             return [''.join(s)]
# #         for i in range(len(alphaPos)):
# #             while queue:
# #                 string = queue.pop()
# #                 pos = alphaPos[i]
# #                 lower = string[:pos]+string[pos].lower()+string[pos+1:]
# #                 upper = string[:pos]+string[pos].upper()+string[pos+1:]
# #                 output.add(lower)
# #                 output.add(upper)
# #                 queue.append(lower)
# #                 queue.append(upper)
# #                 print(queue)
# #         return output
        ans = [[]]
        for char in s:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)
        
    
    
