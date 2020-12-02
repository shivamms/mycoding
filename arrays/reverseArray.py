def reverseArray(nums):
  length = len(nums)
  mid = round(length/2)
  for i in range(mid):
    temp = nums[i]
    nums[i] = nums[length-(i+1)]
    nums[length-(i+1)] = temp
  return nums