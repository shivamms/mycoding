from collections import Counter
class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        return 0 if len(count) < 3 else len(nums) - count[min(count)] - count[max(count)]
        
        
        
            
                
            
        