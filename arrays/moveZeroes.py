#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#must do this in-place without making a copy of the array.
#Minimize the total number of operations.

#O(n)
#iterate through the array
#while iterating, keep track of 
def moveZeroes(nums):
  #zeroescount = 0
  ispreviouszero = False
  minzeroinxex = -1
  for i in range (len(nums)):
    if ispreviouszero and nums[i] != 0:
      nums[minzeroinxex] = nums[i]
      nums[i] = 0
      ispreviouszero = True
      minzeroinxex += 1
    if nums[i] == 0:
      #zeroescount += 1
      if not ispreviouszero:
        minzeroinxex = i
      ispreviouszero = True
  return nums
  
      
