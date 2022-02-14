class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        score = leftScore = leftLeftScore = 0
        prev = -1
        for num in sorted(count):
            if num - 1 != prev:
                score += num * count[num]
            else:
                score = max(leftScore, leftLeftScore + num * count[num])
            prev = num
            temp = leftScore
            leftScore = score
            leftLeftScore = temp
        return score
                
            
                
        