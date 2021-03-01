from collections import Counter
def repeatedDigits(nums, n):
  digitsCount = Counter("".join(str(i) for i in nums))
  mostFrequent = max(val for val in digitsCount.values())
  result = sorted(key for key, val in digitsCount.items() if val == mostFrequent)
  return result

  