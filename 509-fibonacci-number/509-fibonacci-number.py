class Solution:
    fibval = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.fibval:
            return self.fibval[n]
        self.fibval[n] = self.fib(n-1) + self.fib(n-2)
        return self.fibval[n]
        