class Solution(object):
    def maxSubArray(self, nums):
      if len(nums) == 1:
        return nums[0]
      else:
        currentmaximum = 0
        maximum = -100
        for i in range(len(nums)):
          currentmaximum = currentmaximum + nums[i]
          if maximum < currentmaximum:
            maximum = currentmaximum
          if maximum < nums[i]:
            maximum = nums[i]
          if currentmaximum < nums[i]:
            currentmaximum = nums[i]
        return maximum
        