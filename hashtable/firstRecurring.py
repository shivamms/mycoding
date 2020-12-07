def firstRecurring(nums):
  seenNumber = {}
  for i in range(len(nums)):
    if nums[i] in seenNumber.keys():
      return nums[i]
    else:
      seenNumber[nums[i]] = True
  return None


