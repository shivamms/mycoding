class Solution:
    fibval = {0:0, 1:1}
    def fib(self, n: int) -> int:
        # recursion
        # if n in self.fibval:
        #     return self.fibval[n]
        # self.fibval[n] = self.fib(n-1) + self.fib(n-2)
        # return self.fibval[n]
        
        # loop
        # if n <= 1:
        #     return n
        # for i in range(2,n+1):
        #     self.fibval[i] = self.fibval[i-1]+self.fibval[i-2]
        # return self.fibval[n]
    
        # math - Golden Ratio
        gr = (1+math.sqrt(5))/2
        return int(round((gr ** n)/(5 ** 0.5)))
        