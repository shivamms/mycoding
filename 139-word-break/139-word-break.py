class Solution:
    ## recursion
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordDict = set(wordDict)
    #     def checkWord(start):
    #         if start == len(s):
    #             return True
    #         end = start+1
    #         for end in range(start+1, len(s)+1):
    #             if s[start:end] in wordDict and checkWord(end):
    #                 return True
    #         return False
    #     return checkWord(0)
    
    ## DP
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]