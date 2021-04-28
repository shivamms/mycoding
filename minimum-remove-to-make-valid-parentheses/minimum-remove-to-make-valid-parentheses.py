class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stackIndex = []
        for i in range(len(s)):
            if s[i] == "(" or (s[i] == ")" and (len(stackIndex) == 0 or s[stackIndex[-1]] == ")")):
                stackIndex.append(i)
            elif s[i] == ")" and len(stackIndex) > 0 and s[stackIndex[-1]] == "(":
                stackIndex.pop()
        replaceOffset = 0
        for i in range(len(stackIndex)):
            s = s[:stackIndex[i]-replaceOffset] + s[stackIndex[i] -replaceOffset + 1:]
            replaceOffset += 1
        return s
    