class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for d in (nums):
            pos.append(d) if d > 0 else neg.append(d)
        n = len(pos)
        j = 0
        for i in range(n):
            nums[j] = pos[i]
            nums[j+1] = neg[i]
            j += 2
        return nums

        

        
        