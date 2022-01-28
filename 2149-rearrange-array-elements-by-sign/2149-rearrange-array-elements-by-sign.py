class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        res = [0]*len(nums)
        for d in nums:
            if d > 0:
                res[pos] = d
                pos += 2
            elif d < 0:
                res[neg] = d
                neg += 2
        return res

        

        
        