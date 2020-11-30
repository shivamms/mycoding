#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#return maximum sum of contiguous numbers.
#Time: O(n) and Space: O(1)
#start with first number.
#find local maximum by adding to the next number.
#keep updating the global maximum if local maximum is greater than global maximum.
#during any iteration, if global maximum is less than the current number, then update gloabl maximum and local maximum with current number.
#setting up the global and local maximum to current number make sure we disregard the subarray which reduces the sum overall.
#Greedy algorithm
def maxSubArray(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    localmaximum = 0
    globalmaximum = -2^31
    for i in range(len(nums)):
      localmaximum = localmaximum + nums[i]
      if globalmaximum < localmaximum:
        globalmaximum = localmaximum
      if globalmaximum < nums[i]:
        globalmaximum = nums[i]
      if localmaximum < nums[i]:
        localmaximum = nums[i]
    return globalmaximum









        
