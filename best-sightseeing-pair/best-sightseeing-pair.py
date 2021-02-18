class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        k = A[0]-1
        score = 0
        for i in range(1,len(A)):
            score = max(score,A[i]+k)
            k = max(k,A[i])
            k -= 1
        return score
        