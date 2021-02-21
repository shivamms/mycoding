class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lengthA = len(A)
        lengthB = len(B)
        memo = [[0] * (lengthB+1) for _ in range(lengthA+1)]
        for i in range(lengthA-1,-1,-1):
            for j in range(lengthB-1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max([max(row) for row in memo])
        
        