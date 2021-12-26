import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        left, right = [0] * size, [0] * size
        maximums = []
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, size):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = size-i-1
            if (j +1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        print(left, right)

        for i in range(size-k+1):
            maximums.append(max(right[i],left[i+k-1]))

        return maximums
        