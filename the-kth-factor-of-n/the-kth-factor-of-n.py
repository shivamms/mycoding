class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = 1
        counter = 0
        while f <= n:
            if n % f == 0:
                counter += 1
            if counter == k:
                return f
            f += 1
        return -1