class Solution:
    fibval = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        # recursion and memoization
        # if n in self.fibval:
        #     return self.fibval[n]
        # self.fibval[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        # return self.fibval[n]
    
        # loop and memoization
        if n in self.fibval:
            return self.fibval[n]
        for i in range(3,n+1):
            self.fibval[i] = self.fibval[i-3] + self.fibval[i-2] + self.fibval[i-1]
        return self.fibval[n]
        