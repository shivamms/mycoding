class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        
    import random
    def pickIndex(self) -> int:
        return random.choices(range(0,len(self.w)), weights=self.w, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()