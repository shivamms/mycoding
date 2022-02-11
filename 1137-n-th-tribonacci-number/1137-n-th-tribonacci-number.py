class Solution:
    fibval = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.fibval:
            return self.fibval[n]
        self.fibval[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.fibval[n]
        