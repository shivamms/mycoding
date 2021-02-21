def minSubArrayLen(target: int, nums: List[int]) -> int:
    length = 0
    minlength = 0
    sum = 0
    for i in range(len(nums)):
        while sum < target and i < len(nums):
            sum += nums[i]
            length += 1
            i += 1
        if sum >= target:
            if minlength > 0:
                minlength = min(minlength,length)
            else:
                minlength = length
        length = 0
        sum = 0
    return minlength