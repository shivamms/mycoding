#Given an array, rotate the array to the right by k steps, where k is non-negative.

#Follow up:
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#Could you do it in-place with O(1) extra space?

#Example 1:
#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

#Example 2:
#Input: nums = [-1,-100,3,99], k = 2
#Output: [3,99,-1,-100]
#Explanation: 
#rotate 1 steps to the right: [99,-1,-100,3]
#rotate 2 steps to the right: [3,99,-1,-100]
def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a % b)

def rotateArrayRight(nums, k):
    length = len(nums)
    k = k % length
    geeseedi = gcd(k,length)
    for setnumber in range(geeseedi):
        temp = nums[setnumber]
        currentposition = setnumber
        while 1:
            movingposition = currentposition + k
            if movingposition >= length:
                movingposition = movingposition - length
            if movingposition == setnumber:
                break
            nums[currentposition] = nums[movingposition]
            currentposition = movingposition
        nums[currentposition] = temp
    return nums
#print(rotateArrayRight([4,10,12,8,9,18,0,2,11,23,7,13],4))

def rotateArrayLeft(nums, k):
    length = len(nums)
    k = k % length
    geeseedi = gcd(k,length)
    for setnumber in range(geeseedi):
        temp = nums[setnumber]
        currentposition = setnumber
        while 1:
            movingposition = currentposition + length - k
            if movingposition >= length:
                movingposition = movingposition - length
            if movingposition == setnumber:
                break
            nums[currentposition] = nums[movingposition]
            currentposition = movingposition
        nums[currentposition] = temp
    return nums

