class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepCost = {}
        n = len(cost)-1
        def mc(step):
            if step >= n: return 0
            if step in stepCost:
                return stepCost[step]
            stepCost1 = cost[step+1] if step + 1 <= n else 0
            stepCost2 = cost[step+2] if step + 2 <= n else 0
            stepCost1 = stepCost1 + mc(step+1)
            stepCost2 = stepCost2 + mc(step+2)
            stepCost[step] =  min(stepCost1, stepCost2)
            return stepCost[step]
        return mc(-1)