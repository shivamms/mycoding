class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        maxside= 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1], dp[i-1][j]) + 1
                    maxside = max(maxside, dp[i][j])
        return maxside ** 2
# SRTBOT 
# square value of any cell (i,j) is S(i,j)
# subproblems (S) -> S(i,j) = S(i-1,j-1) + 1 for each matrix(i,j) = 1
# relate (R) -> S(i,j) = min(S(i-1,j-1),S(i-1,j),S(i,j-1))+1
# topo order (T) -> i and j increasing
# base (B) -> S(i,j) = 0
# original problem (O) -> max(s(i,j)) for all i and j of matrix
# time (T) -> O(mn)

                        