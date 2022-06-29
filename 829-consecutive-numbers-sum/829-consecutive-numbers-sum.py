class Solution:
    # mathematical notes for this problem
    # N = sum of consecutive numbers
    # N = (x+1)+(x+2)+...+(x+k)
    # N = kx+(1+2+...+k)
    # N = kx+k(k+1)/2
    # N/k = x+(k+1)/2
    # (N/k) - (k+1)/2 = x
    # x = N - (k(k+1)/2)
    # Since x is non-zero positive integer, then we have:
    # N/k >= (k+1)/2
    # 2N >= k**2 + k
    # 2N >= (k+1/2)**2 - 1/4
    # 2N + 1/4 >= (k+1/2)**2
    # (2N + 1/4)**0.5 >= (k + 1/2)
    # k <= (2N + 1/4)**0.5 - 1/2
    # Hence, k is limited to (2N + 1/4)**0.5 - 1/2
    # Our solution is 
    # for k from 1 to (2N + 1/4)**0.5 - 1/2
    # how many cases we have for x = N/k + (k+1)/2 and x > 0. 
    
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upper_limit = ceil((2*n + 0.25)**0.5 - 0.5) + 1 
        for k in range(1, upper_limit):
            if (n - (k * (k+1)) // 2) % k == 0:
                count += 1
        return count