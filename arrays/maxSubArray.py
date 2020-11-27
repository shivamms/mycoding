#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#assume the number are not sorted
#1 <= nums.length <= 2 * 104
#-231 <= nums[i] <= 231 - 1
#[-2,1,-3,4,-1,2,1,-5,4]
"""
def maximumSubarraySimple(arr):
  if len(arr) == 1:
    return arr
  else:
    currentmaximum = 0
    maximum = 0
    currentstart = 0
    currentend = 0
    originalstart= 0
    for i in range(len(arr)):
      currentmaximum = currentmaximum + arr[i]
      if maximum < currentmaximum:
        maximum = currentmaximum
        currentend = i
        originalstart = currentstart
      if currentmaximum < 0:
        currentmaximum = 0
        currentstart = i + 1
    if currentstart > currentend:
      currentstart = originalstart
    if currentend <= 0:
      currentend = len(arr) - 1
    return arr[currentstart:currentend+1]
"""
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






        
