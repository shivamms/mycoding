class Solution:
    
    def climbStairs(self, n: int) -> int:
        steps = {}
        def cs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in steps:
                return steps[i]
            steps[i] =  cs(i+1) + cs(i+2)
            return steps[i]
        
        return cs(0)
            
            
        
        