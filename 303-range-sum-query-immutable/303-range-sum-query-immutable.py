class NumArray:
    def __init__(self, nums: List[int]):
        self.sumArray = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            self.sumArray[i+1] = self.sumArray[i] + nums[i]
    def sumRange(self, left: int, right: int) -> int:
        return self.sumArray[right+1] - self.sumArray[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)