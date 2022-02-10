class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            print(left, pivot, right)
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                print('target is less')
                right = pivot -1
                if left > right:
                    return pivot
            else:
                if left == right:
                    return pivot + 1
                left = pivot + 1